from flask import Blueprint, request, render_template, redirect, url_for, flash
from model.loaisach_model import getloaisach
from model.nhaxuatban_model import getnxb
from model.sach_model import getsach, themsach, suasach, xoasach
from model.tacgia_model import gettacgia

sach_bp = Blueprint('sach', __name__, url_prefix='/sach')

@sach_bp.route('/')
def get_sach():
    sachs = getsach()
    tacgias=gettacgia()
    nhaxuatbans=getnxb()
    loaisachs=getloaisach()
    return render_template('sach.html',sachs=sachs, tacgias=tacgias, nhaxuatbans=nhaxuatbans, loaisachs=loaisachs)

@sach_bp.route('/them', methods=['POST'])
def them_sach():
    maSach = request.form.get('maSach')
    tenSach = request.form.get('tenSach')
    tacGia = request.form.get('tacGia') 
    nhaXuatBan = request.form.get('nhaXuatBan')
    loaiSach = request.form.get('loaiSach')
    soTrang = request.form.get('soTrang')
    giaBan = request.form.get('giaBan')
    soLuong = request.form.get('soLuong')
    hinhAnh = request.form.get('hinhAnh')

    if not maSach:
        flash('Vui lòng nhập mã sách', 'danger')
        return redirect(url_for('sach.get_sach'))
    if not tenSach:
        flash('Vui lòng nhập tên sách', 'danger')
        return redirect(url_for('sach.get_sach'))
    if not soTrang:
        flash('Vui lòng nhập số trang', 'danger')
        return redirect(url_for('sach.get_sach'))
    if not soTrang or not soTrang.isdigit() or int(soTrang) < 10 or int(soTrang) > 1000:
        flash('Số trang sách phải nhập từ 10 đến 1000!', 'danger')
        return redirect(url_for('sach.get_sach'))
    if not giaBan:
        flash('Vui lòng nhập giá bán', 'danger')
        return redirect(url_for('sach.get_sach'))
    if not giaBan or not giaBan.isdigit() or int(giaBan) < 1000 or int(giaBan) > 10000000:
        flash('Giá bán sách phải nhập từ 1.000đ đến 10.000.000đ', 'danger')
        return redirect(url_for('sach.get_sach'))
    if not soLuong:
        flash('Vui lòng nhập số lượng', 'danger')
        return redirect(url_for('sach.get_sach'))
    if not soLuong or not soLuong.isdigit() or int(soLuong) < 1 or int(soLuong) > 500:
        flash('Số lượng sách phải nhập từ 10 đến 500!', 'danger')
        return redirect(url_for('sach.get_sach'))
    if not hinhAnh:
        flash('Vui lòng nhập hình ảnh', 'danger')
        return redirect(url_for('sach.get_sach'))

    message = themsach(maSach, tenSach, tacGia,nhaXuatBan,loaiSach,soTrang,giaBan,soLuong,hinhAnh)
    if message == "Mã sách đã tồn tại":
        flash(message, 'danger')
    elif message == "Thêm sách thành công!":
        flash(message, 'success')
    else:
        flash(message, 'danger')
    return redirect(url_for('sach.get_sach'))

@sach_bp.route('/sua', methods=['POST'])
def sua_sach():
    maSach = request.form.get('maSach')
    tenSach = request.form.get('tenSach')
    tacGia = request.form.get('tacGia')
    nhaXuatBan = request.form.get('nhaXuatBan')
    loaiSach = request.form.get('loaiSach')
    soTrang = request.form.get('soTrang')
    giaBan = request.form.get('giaBan')
    soLuong = request.form.get('soLuong')
    hinhAnh = request.form.get('hinhAnh')

    if not maSach:
        flash('Vui lòng nhập mã sách', 'danger')
        return redirect(url_for('sach.get_sach'))
    if not tenSach:
        flash('Vui lòng nhập tên sách', 'danger')
        return redirect(url_for('sach.get_sach'))
    if not soTrang:
        flash('Vui lòng nhập số trang', 'danger')
        return redirect(url_for('sach.get_sach'))
    if not soTrang or not soTrang.isdigit() or int(soTrang) < 10 or int(soTrang) > 1000:
        flash('Số trang sách phải nhập từ 10 đến 1000!', 'danger')
        return redirect(url_for('sach.get_sach'))
    if not giaBan:
        flash('Vui lòng nhập giá bán', 'danger')
        return redirect(url_for('sach.get_sach'))
    if not giaBan or not giaBan.isdigit() or int(giaBan) < 1000 or int(giaBan) > 10000000:
        flash('Giá bán sách phải nhập từ 1.000đ đến 10.000.000đ', 'danger')
        return redirect(url_for('sach.get_sach'))
    if not soLuong:
        flash('Vui lòng nhập số lượng', 'danger')
        return redirect(url_for('sach.get_sach'))
    if not soLuong or not soLuong.isdigit() or int(soLuong) < 1 or int(soLuong) > 500:
        flash('Số lượng sách phải nhập từ 10 đến 500!', 'danger')
        return redirect(url_for('sach.get_sach'))
    if not hinhAnh:
        flash('Vui lòng nhập hình ảnh', 'danger')
        return redirect(url_for('sach.get_sach'))

    message = suasach(maSach, tenSach, tacGia,nhaXuatBan,loaiSach,soTrang,giaBan,soLuong,hinhAnh)
    if message == "Mã sách không tồn tại":
        flash(message, 'danger') 
    else:
        flash('Cập nhật sách thành công!', 'success') 
    return redirect(url_for('sach.get_sach'))

@sach_bp.route('/xoa/<maSach>', methods=['POST'])
def xoa_sach(maSach):
    message = xoasach(maSach)

    if message == "Xóa sách thành công!":
        flash(message, 'success')
    else:
        flash(message, 'danger')
    return redirect(url_for('sach.get_sach'))