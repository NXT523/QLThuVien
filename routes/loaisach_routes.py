from flask import Blueprint, request, render_template, redirect, url_for, flash
from model.loaisach_model import getloaisach, themloaisach, sualoaisach, xoaloaisach

loaisach_bp = Blueprint('loaisach', __name__, url_prefix='/loaisach')

@loaisach_bp.route('/')
def get_loaisach():
    loaisachs = getloaisach()
    return render_template('loaisach.html', loaisachs=loaisachs)

@loaisach_bp.route('/them', methods=['POST'])
def them_loaisach():
    maLoai = request.form.get('maLoai')
    loaiSach = request.form.get('loaiSach')
    ghiChu = request.form.get('ghiChu')

    if not maLoai:
        flash('Vui lòng nhập mã loại sách', 'danger')
        return redirect(url_for('loaisach.get_loaisach'))
    if not loaiSach:
        flash('Vui lòng nhập tên loại sách', 'danger')
        return redirect(url_for('loaisach.get_loaisach'))

    message = themloaisach(maLoai, loaiSach, ghiChu)
    if message == "Mã loại sách đã tồn tại":
        flash(message, 'danger')
    elif message == "Thêm loại sách thành công!":
        flash(message, 'success')
    else:
        flash(message, 'danger')
    return redirect(url_for('loaisach.get_loaisach'))

@loaisach_bp.route('/sua', methods=['POST'])
def sua_loaisach():
    maLoai = request.form.get('maLoai')
    loaiSach = request.form.get('loaiSach')
    ghiChu = request.form.get('ghiChu')

    if not maLoai:
        flash('Vui lòng nhập mã loại sách', 'danger')
        return redirect(url_for('loaisach.get_loaisach'))
    if not loaiSach:
        flash('Vui lòng nhập tên loại sách', 'danger')
        return redirect(url_for('loaisach.get_loaisach'))
    
    message = sualoaisach(maLoai, loaiSach, ghiChu)
    if message == "Mã loại sách không tồn tại":
        flash(message, 'danger') 
    else:
        flash('Cập nhật loại sách thành công!', 'success') 
    return redirect(url_for('loaisach.get_loaisach'))

@loaisach_bp.route('/xoa/<maLoai>', methods=['POST'])
def xoa_loaisach(maLoai):
    message = xoaloaisach(maLoai)
    if message == "Xóa loại sách thành công!":
        flash(message, 'success')
    else:
        flash(message, 'danger')
    return redirect(url_for('loaisach.get_loaisach'))

