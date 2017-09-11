from . import calculator
from .cargo import optimal_weight
from app import db
from flask import render_template, request, flash, redirect, url_for
from ..models import db, CapWeight, ItemWeight

@calculator.route('/calculator')
def index():
    return render_template('calculator/calculator.html')

@calculator.route('/calculator/new')
def new_calculator():
    db.session.query(CapWeight.capacity).delete()
    db.session.query(ItemWeight.item).delete()
    db.session.commit()
    return render_template('calculator/calculator.html')

@calculator.route('/calculator/add_capacity', methods=['POST', 'GET'])
def add_capacity():
    capacity = request.form.get('capacity', type=int)
    if request.method == 'POST' and capacity is not None:
        db.session.query(CapWeight.capacity).delete()
        entry = CapWeight(capacity=capacity)
        db.session.add(entry)
        db.session.commit()
        flash("Your maximum loading capacity is " + str(capacity))
    else:
        flash('Please enter a valid number')
        return redirect(url_for('calculator.index')) #in case if user refreshes browser. It's called post-redirect-get pattern
    return redirect(url_for('calculator.index')) #should be 'show_result'

@calculator.route('/calculator/add_item', methods=['POST', 'GET'])
def add_item():
    item = request.form.get('item', type=int)
    if request.method == 'POST' and item is not None:
        entry = ItemWeight(item=item)
        db.session.add(entry)
        db.session.commit()
        #flash("You've added " + str(item))
    else:
        flash('Please enter a valid number')
        return redirect(url_for('calculator.index')) #in case if user refreshes browser. It's called post-redirect-get pattern
    return redirect(url_for('calculator.index'))

@calculator.route('/calculator/result')
def result():
    items = ItemWeight.query.filter(ItemWeight.item).all()
    loading_capacity=CapWeight.query.filter(CapWeight.capacity).first()
    #flash('' + str(loading_capacity))
    if items !=[] and (loading_capacity is not None):
        W = loading_capacity.capacity
        array = [i.item for i in items]
        optimal = optimal_weight(W, array)
        db.session.query(CapWeight.capacity).delete()
        db.session.query(ItemWeight.item).delete()
        db.session.commit()
    else:
        flash('Please provide a valid data')
        return redirect(url_for('calculator.index'))
    return render_template('calculator/calculator.html', optimal=str(optimal))
