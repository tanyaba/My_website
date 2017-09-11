from . import majority
from .majority_count import get_majority_element
from app import db
from flask import render_template, request, flash, redirect, url_for
from ..models import Vote, db


@majority.route('/majority')
def vote():
    return render_template('majority/vote.html')


@majority.route('/new_count')
def new_count():
    db.session.query(Vote.product).delete()
    db.session.commit()
    return redirect(url_for('majority.show_result'))


@majority.route('/add', methods=['POST', 'GET'])
def add_entry():
    #db.create_all()
    try:
        if request.method =='POST':
            select=request.form['select'] # name='select' in radio buttons (voting_app.html file)
            entry=Vote(product=str(select))
            db.session.add(entry)
            db.session.commit()
            #flash("You've selected product " + select, 'product')
        else:
            return redirect(url_for('majority.vote')) #in case if user refreshes browser. It's called post-redirect-get pattern
    except:
        flash('No product was selected', 'product')
    return redirect(url_for('majority.show_result')) #should be 'show_result'

@majority.route('/result')
def show_result():
    res=Vote.query.order_by(Vote.product).all()
    array=[i.product for i in res]
    if array!=[]:
        result= get_majority_element(array, 0, len(array)-1)
    else:
        result=''
    return render_template('majority/vote.html', result=result)



