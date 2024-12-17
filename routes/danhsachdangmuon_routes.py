from flask import Blueprint, render_template
from model.danhsachdangmuon_model import getdanhsachdangmuon
from model.quanlybaocaothongke_model import gettongsach, gettongloaisach, gettongtacgia, gettongnhaxuatban, gettongsinhvien, gettongsachmuon, gettongnhanvien

danhsachdangmuon_bp = Blueprint('danhsachdangmuon', __name__, url_prefix='/danhsachdangmuon')

@danhsachdangmuon_bp.route('/')
def get_danhsachdangmuon():
    danhsachdangmuons = getdanhsachdangmuon()
    tongsachs = gettongsach()
    tongloaisachs = gettongloaisach()
    tongtacgias = gettongtacgia()
    tongnhaxuatbans = gettongnhaxuatban()
    tongsinhviens = gettongsinhvien()
    tongsachmuons = gettongsachmuon()
    tongnhanviens = gettongnhanvien()
    return render_template('danhsachdangmuon.html',danhsachdangmuons=danhsachdangmuons, tongsachs=tongsachs, tongloaisachs=tongloaisachs, tongtacgias=tongtacgias, tongnhaxuatbans=tongnhaxuatbans, tongsinhviens=tongsinhviens, tongsachmuons=tongsachmuons, tongnhanviens=tongnhanviens)


