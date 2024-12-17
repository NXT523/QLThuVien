
from flask import Blueprint, request, render_template, redirect, url_for, flash
from model.tacgia_model import gettacgia, themtacgia, suatacgia, xoatacgia

tacgia_bp = Blueprint('tacgia', __name__, url_prefix='/tacgia')

@tacgia_bp.route('/')
def get_tacgia():
    tacgias = gettacgia()
    return render_template('tacgia.html', tacgias=tacgias)

@tacgia_bp.route('/them', methods=['POST'])
def them_tacgia():
    maTacGia = request.form.get('maTacGia')
    tenTacGia = request.form.get('tenTacGia')
    ghiChu = request.form.get('ghiChu')

    if not maTacGia:
        flash('Vui lòng nhập mã tác giả', 'danger')
        return redirect(url_for('tacgia.get_tacgia'))
    if not tenTacGia:
        flash('Vui lòng nhập tên tác giả', 'danger')
        return redirect(url_for('tacgia.get_tacgia'))

    message = themtacgia(maTacGia, tenTacGia, ghiChu)
    if message == "Mã tác giả đã tồn tại":
        flash(message, 'danger')
    elif message == "Thêm tác giả thành công!":
        flash(message, 'success')
    else:
        flash(message, 'danger')
    return redirect(url_for('tacgia.get_tacgia'))

@tacgia_bp.route('/sua', methods=['POST'])
def sua_tacgia():
    maTacGia = request.form.get('maTacGia')
    tenTacGia = request.form.get('tenTacGia')
    ghiChu = request.form.get('ghiChu')

    if not maTacGia:
        flash('Vui lòng nhập mã tác giả', 'danger')
        return redirect(url_for('tacgia.get_tacgia'))
    if not tenTacGia:
        flash('Vui lòng nhập tên tác giả', 'danger')
        return redirect(url_for('tacgia.get_tacgia'))
    
    message = suatacgia(maTacGia, tenTacGia, ghiChu)
    if message == "Mã tác giả không tồn tại":
        flash(message, 'danger') 
    else:
        flash('Cập nhật tác giả thành công!', 'success') 
    return redirect(url_for('tacgia.get_tacgia'))

@tacgia_bp.route('/xoa/<maTacGia>', methods=['POST'])
def xoa_tacgia(maTacGia):
    message = xoatacgia(maTacGia)

    if message == "Xóa loại sách thành công!":
        flash(message, 'success')
    else:
        flash(message, 'danger')
    return redirect(url_for('tacgia.get_tacgia'))