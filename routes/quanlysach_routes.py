from flask import Blueprint, request, render_template
from model.quanlysach_model import getquanlysach

quanlysach_bp = Blueprint('quanlysach', __name__, url_prefix='/quanlysach')

@quanlysach_bp.route('/')
def get_quanlysach():
    quanlysachs = getquanlysach()
    return render_template('quanlysach.html', quanlysachs=quanlysachs)


