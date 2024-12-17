--Xóa Database
IF EXISTS (SELECT name FROM sys.databases WHERE name = 'QLThuVien')
BEGIN
    DROP DATABASE QLThuVien;
END
--Tạo Database
CREATE DATABASE QLThuVien;
GO
USE QLThuVien;
GO
-- Tạo bảng TacGia
CREATE TABLE TacGia (
    MaTacGia NVARCHAR(10) PRIMARY KEY,
    TenTacGia NVARCHAR(50),
    GhiChu NVARCHAR(255)
);

-- Tạo bảng NhaXuatBan
CREATE TABLE NhaXuatBan (
    MaNXB NVARCHAR(10) PRIMARY KEY,
    TenNXB NVARCHAR(50),
    GhiChu NVARCHAR(255)
);

-- Tạo bảng LoaiSach
CREATE TABLE LoaiSach (
    MaLoai NVARCHAR(10) PRIMARY KEY,
    TenLoaiSach NVARCHAR(50),
    GhiChu NVARCHAR(255)
);

-- Tạo bảng Sach
CREATE TABLE Sach (
    MaSach NVARCHAR(10) PRIMARY KEY,
    TenSach NVARCHAR(50),
    MaTacGia NVARCHAR(10) FOREIGN KEY REFERENCES TacGia(MaTacGia),
    MaNXB NVARCHAR(10) FOREIGN KEY REFERENCES NhaXuatBan(MaNXB),
    MaLoai NVARCHAR(10) FOREIGN KEY REFERENCES LoaiSach(MaLoai),
    SoTrang INT,
    GiaBan DECIMAL(18, 2),
    SoLuong INT,
	HinhAnh NVARCHAR(50)
);

-- Tạo bảng NhanVien
CREATE TABLE NhanVien (
    MaNhanVien NVARCHAR(10) PRIMARY KEY,
    TenNhanVien NVARCHAR(50),
    SoDienThoai NVARCHAR(10),
    GioiTinh NVARCHAR(10),
    DiaChi NVARCHAR(100),
    MatKhau NVARCHAR(10),
	VaiTro NVARCHAR(10)
);

-- Tạo bảng SinhVien
CREATE TABLE SinhVien (
    MaSV NVARCHAR(10) PRIMARY KEY,
    TenSV NVARCHAR(50),
    NganhHoc NVARCHAR(50),
    KhoaHoc NVARCHAR(50),
    SoDienThoai NVARCHAR(10)
);

-- Tạo bảng MuonTraSach
CREATE TABLE MuonTraSach (
    MaPhieuMuon INT PRIMARY KEY IDENTITY(1,1),
    MaSV NVARCHAR(10) FOREIGN KEY REFERENCES SinhVien(MaSV),
    MaSach NVARCHAR(10) FOREIGN KEY REFERENCES Sach(MaSach),
    NgayMuon DATE,
    NgayTra DATE,
    GhiChu NVARCHAR(255)
);

INSERT INTO TacGia (MaTacGia, TenTacGia, GhiChu) VALUES 
(N'TG001', N'Nguyễn Nhật Ánh', N'Tác giả nổi tiếng với các tác phẩm về tuổi thơ'),
(N'TG002', N'Trần Đăng Khoa', N'Tác giả của nhiều bài thơ nổi tiếng'),
(N'TG003', N'Tô Hoài', N'Tác giả của Dế Mèn Phiêu Lưu Ký'),
(N'TG004', N'Nam Cao', N'Nhà văn hiện thực phê phán'),
(N'TG005', N'Vũ Trọng Phụng', N'Nhà văn phê phán xã hội');

INSERT INTO NhaXuatBan (MaNXB, TenNXB, GhiChu) VALUES 
(N'NXB001', N'Nhà Xuất Bản Trẻ', N'Chuyên xuất bản sách thiếu nhi và văn học'),
(N'NXB002', N'Nhà Xuất Bản Giáo Dục', N'Chuyên xuất bản sách giáo dục'),
(N'NXB003', N'Nhà Xuất Bản Văn Học', N'Xuất bản sách văn học cổ điển và hiện đại'),
(N'NXB004', N'Nhà Xuất Bản Khoa Học Kỹ Thuật', N'Chuyên xuất bản tài liệu khoa học'),
(N'NXB005', N'Nhà Xuất Bản Thông Tin', N'Chuyên xuất bản các tài liệu tham khảo');

INSERT INTO LoaiSach (MaLoai, TenLoaiSach, GhiChu) VALUES 
(N'LS001', N'Tiểu Thuyết', N'Sách thuộc thể loại tiểu thuyết'),
(N'LS002', N'Giáo Khoa', N'Sách giáo khoa dùng cho học sinh'),
(N'LS003', N'Thơ', N'Sách tập thơ'),
(N'LS004', N'Kỹ Thuật', N'Sách về kỹ thuật và công nghệ'),
(N'LS005', N'Tài Liệu Tham Khảo', N'Các tài liệu dùng để tham khảo');

INSERT INTO Sach (MaSach, TenSach, MaTacGia, MaNXB, MaLoai, SoTrang, GiaBan, SoLuong, HinhAnh) VALUES 
(N'S001', N'Cho tôi xin một vé đi tuổi thơ', N'TG001', N'NXB001', N'LS001', 150, 50000, 20, N'chotoixinmotvedituoitho.jpg'),
(N'S002', N'Dế Mèn Phiêu Lưu Ký', N'TG003', N'NXB001', N'LS001', 200, 70000, 15, N'demen.jpg'),
(N'S003', N'Lão Hạc', N'TG004', N'NXB002', N'LS001', 100, 40000, 10, N'laohac.jpg'),
(N'S004', N'Vợ Nhặt', N'TG005', N'NXB003', N'LS001', 120, 45000, 12, N'vonhat.jpg'),
(N'S005', N'Từ điển tiếng Anh', N'TG002', N'NXB005', N'LS005', 300, 120000, 8, N'tudientienganh.jpg');

INSERT INTO NhanVien (MaNhanVien, TenNhanVien, SoDienThoai, GioiTinh, DiaChi, MatKhau, VaiTro) VALUES 
(N'NV001', N'Nguyễn Văn A', N'0123456789', N'Nam', N'Hà Nội', N'123456', N'NhanVien'),
(N'NV002', N'Trần Thị B', N'0123456780', N'Nữ', N'TP. HCM', N'123456', N'Admin'),
(N'NV003', N'Phạm Văn C', N'0112233445', N'Nam', N'Đà Nẵng', N'654321', N'NhanVien');

INSERT INTO SinhVien (MaSV, TenSV, NganhHoc, KhoaHoc, SoDienThoai) VALUES 
(N'SV001', N'Lê Văn D', N'Công nghệ thông tin', N'K25', N'0123123123'),
(N'SV002', N'Nguyễn Thị E', N'Kinh tế', N'K26', N'0456456456'),
(N'SV003', N'Trần Văn F', N'Y học', N'K25', N'0789789789'),
(N'SV004', N'Đỗ Thị G', N'Luật', N'K27', N'0321321321'),
(N'SV005', N'Phan Văn H', N'Văn học', N'K26', N'0654654654');

INSERT INTO MuonTraSach (MaSV, MaSach, NgayMuon, NgayTra, GhiChu) VALUES 
(N'SV001', N'S001', '2024-10-01', '2024-10-10', N'Sách mới'),
(N'SV002', N'S002', '2024-09-15', '2024-09-25', N'Sách mới'),
(N'SV003', N'S003', '2024-08-20', '2024-09-01', N'Sách hỏng một phần'),
(N'SV004', N'S004', '2024-10-05', '2024-10-15', N'Sách cũ'),
(N'SV005', N'S005', '2024-07-30', '2024-08-10', N'Sách mới');



