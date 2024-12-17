from flask import Blueprint, request, render_template, redirect, url_for, flash
from model.nhaxuatban_model import getnxb, themnxb, suanxb, xoanxb

nhaxuatban_bp = Blueprint('nhaxuatban', __name__, url_prefix='/nhaxuatban')

@nhaxuatban_bp.route('/')
def get_nxb():
    nhaxuatbans = getnxb()
    return render_template('nhaxuatban.html', nhaxuatbans=nhaxuatbans)

@nhaxuatban_bp.route('/them', methods=['POST'])
def them_nxb():
    maNXB = request.form.get('maNXB')
    tenNXB = request.form.get('tenNXB')
    ghiChu = request.form.get('ghiChu')

    if not maNXB:
        flash('Vui lòng nhập mã NXB', 'danger')
        return redirect(url_for('nhaxuatban.get_nxb'))
    if not tenNXB:
        flash('Vui lòng nhập tên NXB', 'danger')
        return redirect(url_for('nhaxuatban.get_nxb'))

    message = themnxb(maNXB, tenNXB, ghiChu)
    if message == "Mã loại sách đã tồn tại":
        flash(message, 'danger')
    elif message == "Thêm nxb thành công!":
        flash(message, 'success')
    else:
        flash(message, 'danger')
    return redirect(url_for('nhaxuatban.get_nxb'))

@nhaxuatban_bp.route('/sua', methods=['POST'])
def sua_nxb():
    maNXB = request.form.get('maNXB')
    tenNXB = request.form.get('tenNXB')
    ghiChu = request.form.get('ghiChu')

    if not maNXB:
        flash('Vui lòng nhập mã NXB', 'danger')
        return redirect(url_for('nhaxuatban.get_nxb'))
    if not tenNXB:
        flash('Vui lòng nhập tên NXB', 'danger')
        return redirect(url_for('nhaxuatban.get_nxb'))

    message = suanxb(maNXB, tenNXB, ghiChu)
    if message == "Mã NXB không tồn tại":
        flash(message, 'danger')
    elif message == "Cập nhật nxb thành công!":
        flash(message, 'success')
    else:
        flash(message, 'danger')
    return redirect(url_for('nhaxuatban.get_nxb'))

@nhaxuatban_bp.route('/xoa/<maNXB>', methods=['POST'])
def xoa_nxb(maNXB):
    message = xoanxb(maNXB)
    if message == "Xóa nxb thành công!":
        flash(message, 'success')
    else:
        flash(message, 'danger')
    return redirect(url_for('nhaxuatban.get_nxb'))
