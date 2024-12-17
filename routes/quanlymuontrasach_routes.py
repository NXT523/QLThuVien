from flask import Blueprint, flash, redirect, render_template, request, url_for
from model.quanlymuontrasach_model import getmuontrasach, muonsach, trasach, giahan_ngaytra
from model.quanlysach_model import getquanlysach
from model.sach_model import getsach
from model.quanlysinhvien_model import getsinhvien

quanlymuontrasach_bp = Blueprint('quanlymuontrasach', __name__, url_prefix='/quanlymuontrasach')

@quanlymuontrasach_bp.route('/')
def get_quanlymuontrasach():
    quanlysachs = getquanlysach()
    sachs = getsach()
    quanlysinhviens = getsinhvien()
    muontrasachs = getmuontrasach()
    return render_template('quanlymuontrasach.html', quanlysachs=quanlysachs, sachs=sachs, muontrasachs=muontrasachs, quanlysinhviens=quanlysinhviens)

@quanlymuontrasach_bp.route('/muon', methods=['POST'])
def them_muonsach():
    txtMaSV = request.form['maSinhVien']
    txtMaSach = request.form['tenSach']
    txtNgayMuon = request.form['ngayMuon']
    txtNgayTra = request.form['ngayTra']
    txtGhiChu = request.form['ghiChu']

    message = muonsach(txtMaSV, txtMaSach, txtNgayMuon, txtNgayTra, txtGhiChu)
    if message == "Mượn sách thành công":
        flash('Mượn sách thành công!', 'success')
    elif message.startswith("error:"):
        error_detail = message.split("error:")[1].strip()
        flash(f" {error_detail}", 'error')  
    else:
        flash("Có lỗi không xác định xảy ra!", 'error')
    return redirect(url_for('quanlymuontrasach.get_quanlymuontrasach'))

@quanlymuontrasach_bp.route('/tra/<int:maPhieuMuon>', methods=['POST'])
def tra_sach(maPhieuMuon):
    message = trasach(maPhieuMuon)
    
    if message.startswith("success"):
        flash("Trả sách thành công", "success")
    elif message.startswith("error"):
        flash(message.split(":")[1], "error")
    return redirect(url_for('quanlymuontrasach.get_quanlymuontrasach'))

@quanlymuontrasach_bp.route('/giahan/<int:maPhieuMuon>', methods=['POST'])
def gia_han_sach(maPhieuMuon):
    txtNgayTraMoi = request.form['ngayTraMoi']
    message = giahan_ngaytra(maPhieuMuon, txtNgayTraMoi)

    if message.startswith("success"):
        flash("Gia hạn ngày trả sách thành công", "success")
    elif message.startswith("error"):
        flash(message.split(":")[1], "error")
    return redirect(url_for('quanlymuontrasach.get_quanlymuontrasach'))