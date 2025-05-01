numpy là thư viện giúp xử lí số học, đại số tuyến tính, ma trậnt, tensor (mảng nhiều chiều), …

matplotlib là thư viện giúp vẽ đồ thị, biểu đồ, hình ảnh, …
pandas là thư viện giúp xử lí dữ liệu dạng bảng, dữ liệu chuỗi thời gian, …

numpy tốc độ tính toán sẽ nhanh hơn so với tự cài

để chuyển từ matran sang vector sẽ dùng hàm reshape



thư viện trực quan hóa dữ liệu matplotlib
có thể vẽ dưới dạng đường, dạng điểm (scatter) (hàm plot)
nếu không muốn vẽ rời rạc mà muốn đưa về cùng một cụm biểu diễn
thì ta sẽ vẽ với subplot (diagram,)



thư viện sử lý dữ liệu dạng bảng nổi tiếng là pandas
tạo dataframe , khai báo cột, các list, Index
load dữ liệu từ file csv, excel, sql,( bảng)
quy ước : variable là cột, observation là mẫu quan sát, chỉ mục , cột

gom nhóm dữ liệu với phương thức pivot
stocks.pivot(index='Date', columns='Symbol', values='Close')

gom nhóm dữ liệu với phương thức pivot_table
stocks.pivot_table(index='Date', columns='Symbol', values=['Close', 'Volume'], aggfunc= np.mean )

nối dữ liệu theo chiều dọc với concat (mặc định axis=0)
nơi dữ liệu theo chiều ngang với concat (axis=1)

nếu nó không khớp với nhau về cột thì sẽ thêm NaN
có hỗ trợ điền giá trị khuyết với fillna (value)
lấy tập con theo dòng , vd: sub_df = df1[df1.Y > 0]
sub_df = df1[df1.X.isin([1, 2, 3])]
lấy tập con theo cột, vd: columns = df1[['X', 'Y']]

tạo thêm cột mới với hàm stocks: vd stocks['Volume_Millions'] = stocks['Volume'] / 1000000


vẽ biểu đồ đơn giản
hàm plot và scatter của pandas
df.plot.hist()
df.plot.scatter(x='X', y='Y')


##############################
import numpy as np
a = np.array([1, 2, 3]) # tạo mảng 1 chiều [1, 2, 3]
b = np.array([[1, 2, 3], [4, 5, 6]]) # tạo mảng 2 chiều 
c = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]]) # tạo mảng 3 chiều
type (a) # kiểm tra kiểu dữ liệu
a.shape # kiểm tra kích thước
a[0] # truy cập phần tử

khởi tạo giá trị cho trước
np.ones ((3, 3)) # tạo mảng 3x3 với tất cả giá trị là 1
np.zeros ((3, 3)) # tạo mảng 3x3 với tất cả giá trị là 0   
np.random.random (3) # tạo mảng 3 phần tử với giá trị ngẫu nhiên từ 0 đến 1
np.ones ((4,3,2)) # tạo mảng 3 chiều 4x3x2 với tất cả giá trị là 1
d = np.ones ((3, 3)) * 4 # tạo mảng 3x3 với tất cả giá trị là 4
e = np.eye (3) # tạo ma trận đơn vị 3x3
f = np.arange (0, 10, 2) # tạo mảng từ 0 đến 10 với bước nhảy 2 
g = np.linspace (0, 10, num = 5) # tạo mảng từ 0 đến 10 với 5 phần tử   

np.hstack ((a, b)) # nối mảng theo chiều ngang
np.vstack ((a, b)) # nối mảng theo chiều dọc

data[0:2] # lấy dòng từ 0 đến 2
data [1:] # lấy dòng từ 1 đến hết
data [:2] # lấy dòng từ đầu đến 2
data [0:2, 1] # lấy dòng từ 0 đến 2, cột 1 

b1 = a1[:2, 1:3] # lấy dòng từ 0 đến 2, cột từ 1 đến 3
b1[0, 0] = 77 # b1 là tham chiếu, thay đổi giá trị phần tử 0,0 của b1
a1[0, 1] # giá trị phần tử 0,1 của a1 cũng thay đổi

row_r1 = a1[1, :] # Cùng nội dung là hàng thứ 2, chiều của array là 1
row_r2 = a1[1:2, :] # Cùng nội dung là hàng thứ 2, chiều của array là 2
row_r3 = a1[[1], :] # Cùng nội dung là hàng thứ 2, chiều của array là 2 
tương tự với trên cột
col_r1 = a1[:, 1]
col_r2 = a1[:, 1:2]

print (a[[0,1,2], [0,1,0]]) tương đương với print (np.array([a[0, 0], a[1, 1], a[2, 0]]))

bool_idx = (a > 2) # tạo mảng boolean với điều kiện
print (bool_idx) # in ra mảng boolean
print (a[bool_idx]) # lấy giá trị thỏa điều kiện
hoặc có thể viết gọn print (a[a > 2])

print (np.argmax(a)) # trả về chỉ số của phần tử lớn nhất   
print (np.argmin(a)) # trả về chỉ số của phần tử nhỏ nhất
print (np.mean(a)) # trả về giá trị trung bình
print (np.argsort(a)) # trả về chỉ số của mảng đã sắp xếp
print (np.argsort(a)[::-1]) # trả về chỉ số của mảng đã sắp xếp theo chiều ngược lại    
print (np.where(a > 2)) # trả về chỉ số của phần tử thỏa điều kiện
print (np.where(a > 2)[0]) # trả về chỉ số hàng của phần tử thỏa điều kiện
print (np.where(a >= a[np.argmax(a)])[0]) # trả về chỉ số hàng của phần tử lớn nhất

có thể để numpy tự chọn Kiểu dữ liệu hoặc chọn kiểu dữ liệu
z = np.array([1, 2], dtype=np.int64)

các hàm toán học có sẵn
%%time # đo thời gian thực thi
np.sum(a) # tổng các phần tử
bất cứ khi nào có thể, cố gắng use các phép toán vector hóa
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
print (x + y)  hoặc print (np.add(x, y)) # [5, 7, 9]
print (x - y)  hoặc print (np.subtract(x, y)) # [-3, -3, -3]
print (x * y)  hoặc print (np.multiply(x, y)) # [4, 10, 18]
print (x / y)  hoặc print (np.divide(x, y)) # [0.25, 0.4, 0.5]
print (np.sqrt(x)) # [1.0, 1.41421356, 1.73205081]  
nếu muốn nhân ma trận được với nhau thì số cột của ma trận 1 phải bằng số hàng của ma trận 2    
print (np.dot(x, y)) hoặc print (x.dot(y)) hoặc print (x @ y) # 32

ngoài ra còn có các hàm tính toán trên array như
x = np.array([[1, 2], [3, 4]])
print (np.sum(x)) # tính tổng các phần tử
print (np.min(x)) # tính giá trị nhỏ nhất của các phần tử   
print (np.max(x)) # tính giá trị lớn nhất của các phần tử
còn có tham số axis để tính theo hàng hoặc cột
print (np.sum(x, axis=0)) # [4, 6] tính max theo cột
print (np.sum(x, axis=1)) # [3, 7] tính max theo hàng
ngoài ra còn nhiều hàm mathematical functions có thể tham khảo trên trang chủ của numpy


để thay đổi kích thước trên array, thao tác đơn giản nhất là chuyển vị
x = np.array([[1, 2], [3, 4]])
print (x.T) # chuyển vị ma trận
có thể dùng hàm reshape
data.reshape(2, 3) # chuyển sang 2x3
data.reshape (-1, ) # chuyển sang 1 chiều (vector)
tương tự cho hàm squeeze: data.squeeze() 

để chuyển từ 1D sang 2D array, ta có thể thêm vào một chiều nữa với kích thước là 1
x = np.array([1, 2, 3])
y = x.reshape(-1, 1) # chuyển thành 3 hàng, 1 cột


Broadcasting
là cách numpy xử lý các phép toán giữa các mảng có kích thước khác nhau
Quy tắc 1: nếu hai array khác số chiều, kích thước của array với số chiều (dimension) nhỏ hơn sẽ được chèn thêm 1 về phía đầu bên trái
ví dụ sau, array a sẽ được ngầm mở rộng từ shape từ (3,):1 chiều,  thành shape (1, 3) :2 chiều
a = np.array([1, 2, 3]) # shape (3,)
b = np.array([[4], [5], [6]]) # shape (3, 1)
print (a + b) # kết quả sẽ là shape (3,3), 2 chiều
Quy tắc 2: nếu shape của hai array không khớp nhau ở một chiều nào đó, array nào có kích thước chiều bằng 1 sẽ được kéo dài ở chiều đó để khớp với array còn lại
a = np.array ([1], [2], [3]) # shape (3, 1), sẽ ngầm kéo dài thành (3, 2) để khớp với b
[1, 1]
[2, 2]
[3, 3]
b = np.array ([4, 5], [6, 7], [8, 9]) # shape (3, 2)
print (a + b) # kết quả sẽ là shape (3, 2), kết quả là [[5, 6]
                                                        [8, 9]
                                                        [11, 12]]
Quy tắc 3: nếu hai array không có chiều nào bằng nhau và không có chiều nào kích thước bằng 1 thì báo lỗi
a = np.array([1], [2], [3]) # shape (3, 1)
b = np.array([4, 5], [6, 7]) # shape (2, 2)


#######################################################
import matplotlib.pyplot as pltv (matplotlib là một thư viện để trực quan hóa bằng cách vẽ các dữ liệu kết quả tính toán, với module quan trọng nhất là matplotlib.pyplot)
PLOTTING (Cho phép vẽ dữ liệu 2D dưới dạng đường thẳng)
X = np.arange(0, 3 * np.pi, 0.1) # tạo mảng từ 0 đến 3*pi với bước nhảy 0.1
Y = np.sin(X) # tạo mảng sin
Z = np.cos(X) # tạo mảng cos
plt.plot(X, Y) # vẽ đồ thị sin
plt.plot(X, Z , lable='cos') # vẽ đồ thị cos
plt.xlabel('X axis label') # tên trục X
plt.ylabel('Y axis label') # tên trục Y
plt.title('Sin and Cos') # tiêu đề
plt.legend() # hiển thị chú thích   
plt.show() # hiển thị đồ thị

SCATTER (vẽ dưới dạng điểm rời rạc, không điểm nào nối điểm nào)
x = np.random.rand(100) # tạo mảng 100 phần tử ngẫu nhiên
y = np.random.rand(100) # tạo mảng 100 phần tử ngẫu nhiên
colors = np.random.randint(0, 2, 100) # tạo mảng 100 phần tử ngẫu nhiên từ 0 đến 2
plt.scatter(x, y, c=colors) # vẽ scatter plot
plt.show() # hiển thị đồ thị

SUBPLOT (vẽ nhiều đồ thị trong cùng 1 hình)
X = np.arange(0, 3 * np.pi, 0.1) # tạo mảng từ 0 đến 3*pi với bước nhảy 0.1 
y_sin = np.sin(X) # tạo mảng sin
y_cos = np.cos(X) # tạo mảng cos
plt.subplot(2, 1, 1) # tạo subplot 2 hàng, 1 cột, vẽ đồ thị ở vị trí 1
vẽ lên ô đầu tiên
plt.plot(X, y_sin) # vẽ đồ thị sin
plt.title('Sin') # tiêu đề
kích hoạt ô thứ 2 sau đó vẽ lên ô này
plt.subplot(2, 1, 2) # tạo subplot 2 hàng, 1 cột, vẽ đồ thị ở vị trí 2
plt.plot(X, y_cos) # vẽ đồ thị cos
plt.title('Cos') # tiêu đề
điều chỉnh khoảng cách giữa các ô
plt.subplots_adjust(hspace=0.5) # khoảng cách giữa các ô  
plt.show() # hiển thị đồ thị
ngoài ra có thể tham khảo thêm ở trang chủ của matplotlib


CHART TYPES
scatter plot: vẽ dữ liệu dưới dạng điểm rời rạc
lines: plot
bar plot: vẽ dữ liệu dưới dạng cột
histogram: vẽ dữ liệu dưới dạng biểu đồ cột
pie chart: pie vẽ dữ liệu dưới dạng biểu đồ tròn
vd:
plt.subplot(221) # tạo subplot 2 hàng, 2 cột, vẽ đồ thị ở vị trí 1
plt.scatter(x, y, maker='o') # vẽ scatter plot
plt.subplot(222) # tạo subplot 2 hàng, 2 cột, vẽ đồ thị ở vị trí 2
plt.plot(x, y) # vẽ plot
plt.subplot(223) # tạo subplot 2 hàng, 2 cột, vẽ đồ thị ở vị trí 3
plt.bar(x, y) # vẽ bar plot
plt.subplot(224) # tạo subplot 2 hàng, 2 cột, vẽ đồ thị ở vị trí 4
labels = ['A', 'B', 'C', 'D'] # tạo nhãn
sizes = [15, 30, 45, 10] # tạo kích thước
plt.pie(sizes, labels=labels, autopct='%1.1f%%') # vẽ pie chart với tỷ lệ phần trăm 1 số thập phân
plt.show() # hiển thị đồ thị

Đọc, hiển thị ảnh
from matplotlib.cbook import get_sample_data
img = np.imread(get_sample_data('grace_hopper.png')) # đọc ảnh grace_hopper.png 
plt.imshow(img) # hiển thị ảnh




######################################
PANDAS (tham khảo Pandas_cheat_sheet.pdf)
import pandas as pd
gồm creating DataFrames, Reshaping Data, Method chaining, Summarize Data, Handling Missing data, group data, combine data sets