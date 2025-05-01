1, phát hiện & xử lý dữ liệu bị thiếu
cách tiếp cận phát hiện
hàm isnull() / isna() để kiểm tra dữ liệu bị thiếu
df.isnull().sum() # kiểm tra số lượng dữ liệu bị thiếu trong từng cột

xử lý dữ liệu bị thiếu

- loại bỏ dòng có dữ liệu bị thiếu
df.dropna() # loại bỏ dòng có dữ liệu bị thiếu
df.dropcolna() # loại bỏ cột có dữ liệu bị thiếu

thay thế đơn biến, đa biến, chuỗi thời gian: sklearn-imputation 
- sử dụng các mô hình máy học để dự đoán (KNN (thay thế giá trị bị thiếu bằng giá trị trung bình hoặc tổng trọng số của K láng giềng trogn không gian đặc trưng),...)
- cách tiếp cận khác: tạo cột mới chứa thông tin có giá trị bị thiếu


các pp thay thế giá trị bị thiếu
- thay thế đặc trưng đơn biến (thay thế giá trị bị thiếu bằng giá trị trung bình, trung vị hoặc mode (giá trị xuất hiện nhiều nhất) của một biến)
- phép nội suy tuyến tính (thay thế giá trị bị thiếu bằng giá trị được nội suy tuyến tính trên các điểm ko bị thiếu lân cận)
- thay thế bằng phương pháp hồi quy (ước tính giá trị thiếu bằng cách khớp mô hình hồi quy sử dụng các biến khác làm yếu tố dự đoán)
- thay thế dựa trên mô hình (dùng các mô hình máy học để ước tính giá trị thiếu dựa trên các biến khác trong tập dữ liệu)

2 , phát hiện & xử lý dữ liệu ngoại lai
 phát hiện tiếp cận
 + phương pháp thống kê (EDA) (tính trung bình và độ lệch chuẩn để xác định các giá trị ngoại lai với dữ liệu dạng Gaussian, sử dụng IQR để xác định các giá trị ngoại lai với dữ liệu không phân phối chuẩn,...)
 + tự động phát hiện ngoại lệ (pp Local Outlier Factor, Isolation Forest, EllipicEnvelope, One-Class SVM,...)
 + công cụ phát hiện ngoại lệ (CleanLab, tìm OOD, phát hiện vấn đề dữ liệu,...)


    xử lý dữ liệu ngoại lai
    -loại bỏ
    -thay thế đơn giản (hằng số, mean, median, mode,...)
    -sử dụng mô hình dự đoán (KNN, Linear Regression, hoặc các pp phi tuyến khác)
    
    
    một số pp làm sạch dữ liệu khác
    #Re indexing (Đánh lại chỉ mục)
    data.set_index("column_name", inplace=True) # set index cho dataframe
    data.reset_index(drop=True) #điều này giúp truy cập dữ liệu nhanh hơn
    
    
    #Re formatting (Định dạng lại dữ liệu)
    data['column_name'] = data['column_name'].astype('int') # chuyển đổi kiểu dữ liệu của cột thành dạng số để xử lí tính toán
    
    #Correcting inconsistent data (Sửa lỗi dữ liệu không nhất quán)
    data['column_name'] = data['column_name'].replace(old_value, new_value, inplace=True) # thay thế giá trị cũ bằng giá trị mới trong cột
    
    #Removing duplicates (Xóa dữ liệu trùng lặp)
    data.drop_duplicates()
    
    #Drop unnecessary columns (Xóa cột không cần thiết)
    data.drop(columns=[list_of_columns], axis=1)
    
    #Drop/Filter unnecessary rows (Xóa hàng không cần thiết)
    data.drop([0, 1, 2], inplace=True) # xóa các hàng có chỉ số 0, 1, 2
    data[data["column_name"] == "value"] # lọc các hàng có giá trị cụ thể trong cột
    
    
3, tạo đặc trưng mới - feature extraction
- biến đổi toán học tạo ra các đặc trưng mới từ các đặc trưng hiện có (nhân, chia, cộng, trừ,...)
- đếm số lần xuất hiện của các giá trị trong một cột (count, sum, mean,...)
- tổng hợp đặc trưng theo nhiều cột (groupby, pivot_table,...)

phân rã đặc trưng
một số đặc trưng ở dạng chuỗi phức tạp, nhưng có cấu trúc (vd: địa chỉ, tên, số điện thoại,...), có thể tách thành nhiều cột (đặc trưng) khác nhau để dễ dàng phân tích hơn

tổng hợp đặc trưng
có thể tạo đặc trưng tổng hợp từ nhiều đặc trưng thành phần

tổng hợp theo nhóm
tổng hợp thông tin trên nhiều dòng dữ liệu, thực hiện theo nhóm
sử dụng groupby, tổng hợp theo "mean", "max", "min", "sum", "count",...

đặc trưng cụm
dựa trên phân cụm của một/một số đặc trưng trong tập dữ liệu, có thể tạo ra các đặc trưng mới từ các cụm đã được phân loại

đặc trưng thành phần chính (PCA - Principal Component Analysis) 
giúp loại bỏ các đặc trưng không cần thiết, giảm số chiều của dữ liệu, giúp tăng tốc độ xử lý và cải thiện độ chính xác của mô hình. 
các đặc trưng thành phần chính của dữ liệu có thể magn lại nhiều thoogn tin hơn các đặc trưng ban đầu => phân tích thành phần chính


4, biến đổi đặc trưng - feature transformation
Tại sao cần biến đổi đặc trưng:
    - Yêu cầu loại dữ liệu đầu vào của mô hình:
        + nhiều mô hình yêu cầu dữ liệu dạng số, trogn khi đặc trưng có thể ở dạng khác nhau
        + biến đổi dữ liệu từ dạng khác về dạng số (hay gì đó) để có thể đưa vào mô hình 
        vd: Decision tree cần dữ liệu dạng rời rạc để hoạt động hiệu quả, hoặc logistic/linear regression cần dữ liệu dạng số 
        
    - Giả định về dữ liệu đầu vào của mô hình:
        + nhiều mô hình máy học đặt giả định về phân bố và tỉ lệ (scale) của dữ liệu đầu vào
        + biến đổi từ dữ liệu gốc về các tỉ lệ/phân bố giả định của mô hình (normalize/ scale dữ liệu) -> chính xác hơn, học nhanh hơn
        
    - Vấn đề về dữ liệu nhiễu:
        + nhiều mô hình máy học nhạy cảm với dữ liệu nhiễu (outliers)
        + biến đổi dữ liệu để giảm thiểu ảnh hưởng của nhiễu đến mô hình (vd: log-transform, robust scaling,...)
        
    -Vấn đề về giải thích kết quả:
        + đặc trưng có giá trị liên tục có thể làm mô hình khó hiểu/giải thích (dạng phân loại thì dễ giải thích hơn)
        + binning transformation -> chia khoảng giá trị -> mỗi khoảng có một ý nghĩa
        
    - Vấn đề về quan hệ phi tuyến giữa các đặc trưng:
        +Quan hệ phi tuyến làm cho mô hình hóa và giải thích trở nên khó khăn hơn
        + biến đổi để chuyển về dạng tuyến tính: log transform -> đơn giản hơn
        + VD: Y = b * exp(a*X) -> log (Y) = log (b) + a*X
        
        
Biến đổi đặc trưng
    - Biến đổi dữ liệu dạng số:
        + Min-Max Scaling (chuẩn hóa dữ liệu về khoảng [0,1]): x' = (x - min) / (max - min)
        + Standardization (Z score normalization): chuẩn hóa dữ liệu về phân phối chuẩn N(mean=0, std=1): x' = (x - mean) / std (với x là data point, muy là mean, std là standard deviation)
        + Robust Scaling: chuẩn hóa dữ liệu với các đặc trưng có phân phối không chuẩn (nên không nhạy cảm với outliers): x' = (x - median) / IQR (với IQR là khoảng giữa 25% và 75% của dữ liệu: Q3-Q1)
        + Log Transformation: biến đổi dữ liệu về dạng logarit để giảm thiên lệch và tăng tính đồng nhất của dữ liệu: vd x' = log(x + 1) (thêm 1 để tránh log(0))
        + Rời rạc hóa (Discretization hoặc Binning): chia dữ liệu (dạng số hay liên tục sao đó) thành các khoảng rời rạc (bin) để hiệu quả với mô hình: vd x' = binning(x, bins=10) (chia dữ liệu thành 10 khoảng)
        
    - Biến đổi dữ liệu dạng danh mục (phân loại):
        + One-Hot Encoding: chuyển đổi các giá trị phân loại thành các biến nhị phân (0/1) để đưa vào mô hình: vd pd.get_dummies(df, columns=['column_name'])
        + Label Encoding: chuyển đổi các giá trị phân loại (không nhất thiết phải có tính thứ tự) thành các số nguyên để đưa vào mô hình: vd from sklearn.preprocessing import LabelEncoder; encoder = LabelEncoder(); df['column_name'] = encoder.fit_transform(df['column_name'])
        + Ordinal Encoding: chuyển đổi các giá trị phân loại có thứ tự thành các số nguyên theo thứ tự: vd từ thấp đến cao (hoặc ngược lại): vd df['column_name'] = df['column_name'].map({'low': 1, 'medium': 2, 'high': 3})
        + Target Encoding: chuyển đổi các giá trị phân loại thành giá trị trung bình của biến mục tiêu (target variable) cho mỗi giá trị phân loại: vd df['column_name'] = df.groupby('column_name')['target'].transform('mean')

5, chọn lựa đặc trưng - feature selection
Tại sao cần chọn lựa đặc trưng:
    - Vấn đê về độ chính xác của mô hình:
        + nhiều đặc trưng không cần thiết có thể làm giảm độ chính xác của mô hình (noise, overfitting,...)
        + chỉ chọn đặc trưng phù hợp -> giảm nhiễu -> tăng độ chính xác
        
    - Vấn đề overfitting:
        + Mô hình phức tạp hấp thụ các đặc trưng nhiễu nhiều hơn mô hình đơn giản -> accuracy thấp
        + Loại bỏ các đặc trưng nhiễu -> giảm độ phức tạp của mô hình -> giảm overfitting
        
    - Vấn đề về thời gian và chi phí huấn luyện:
        + nhiều đặc trưng làm mô hình phức tạp hơn -> thời gian và chi phí huấn luyện cao hơn
        + chỉ chọn các đặc trưng cần thiết -> giảm thời gian và chi phí huấn luyện
        
    - Vấn đề về giải thích mô hình:
        + nhiều đặc trưng làm cho mô hình khó hiểu và giải thích (cho khách hàng)
        + chỉ chọn các đặc trưng quan trọng -> dễ giải thích và hiểu lí do ra quyết định của mô hình
        
Một số kỹ thuật chọn lựa đặc trưng:
    - Phương pháp filter (lọc): 
        thỏa mãn các tiêu chí nhất định:
           + Correlation coefficient: Pearson,...: tính toán hệ số tương quan giữa các đặc trưng và biến mục tiêu (target variable) để xác định độ liên quan
           + Variance threshold: loại bỏ các đặc trưng có độ biến thiên thấp (không có nhiều thông tin)
           + Missing value ratio: loại bỏ các đặc trưng có tỷ lệ dữ liệu bị thiếu cao (không đáng tin cậy)
           + Mutual information: tính toán độ tương hỗ giữa các đặc trưng và biến mục tiêu để xác định độ liên quan
           
        Tập đặc trưng -> Các tiêu chí chọn đặc trưng-> chọn tập con các đặc trưng-> Mô hình máy học-> Hiệu quả của mô hình
        
    - Phương pháp wrapper:
        + Forward selection: bắt đầu với một tập hợp rỗng và thêm các đặc trưng vào cho đến khi không còn cải thiện độ chính xác của mô hình
        + Backward elimination: bắt đầu với tất cả các đặc trưng và loại bỏ các đặc trưng không cần thiết cho đến khi không còn cải thiện độ chính xác của mô hình
        + Recursive feature elimination (RFE): sử dụng một mô hình để đánh giá độ quan trọng của các đặc trưng và loại bỏ các đặc trưng không cần thiết theo từng bước
        
      Tập đặc trưng-> Chọn tập con các đặc trưng-> Mô hình máy học (dựa vào độ hiệu quả sẽ quay lại bước chọn tập con các đặc trưng rồi chạy lại)-> Hiệu quả của mô hình
    - Phương pháp embedded:
        + LASSO (L1 regularization): thêm một hình phạt L1 vào hàm mất mát để loại bỏ các đặc trưng không cần thiết
        + Ridge regression (L2 regularization): thêm một hình phạt L2 vào hàm mất mát để giảm độ phức tạp của mô hình
        + Elastic Net: kết hợp cả L1 và L2 regularization để loại bỏ các đặc trưng không cần thiết và giảm độ phức tạp của mô hình
        + Tree-based methods (Random Forest, GBM,... XGBoost): sử dụng độ quan trọng của các đặc trưng được tính toán từ các mô hình cây quyết định để chọn lựa các đặc trưng quan trọng
    - Phương pháp giảm chiều:
        + Component/ Factor based: Factor Analysis, PCA, ICA: sử dụng các phương pháp phân tích thành phần chính (PCA) hoặc phân tích nhân tố (FA) để giảm số chiều của dữ liệu
        + Projection based: t-SNE, UMAP: sử dụng các phương pháp chiếu dữ liệu vào không gian thấp hơn để giảm số chiều của dữ liệu

    tập đặc trưng -> Embedded (nhúng)/ giảm chiều -> Mô hình học (pp nhúng tức chọn lựa đặc trưng đc ngầm thực hiện và đánh giá trong mô hình máy học ) , chọn đặc trưng và đánh giá hiệu quả
    
    
Chi tiết phương pháp
pp 1: Phương pháp lọc (Filter method)
    - Áp dụng một loại chỉ số để loại bỏ các đặc trưng không cần thiết dựa vào
    các tiêu chí nhất định:
        + Hệ số tương quan (Correlation coefficient): Pearson, Spearman, Kendall,...: tính toán hệ số tương quan giữa các đặc trưng và biến mục tiêu (target variable) để xác định độ liên quan
          nếu hai biến tương quan quá ngưỡng thì có thể bỏ một trong hai biến đó đi
        + Ngưỡng phương sai- valiance threshold: loại bỏ các đặc trưng có độ biến thiên thấp (không có nhiều thông tin)
        + Tỷ lệ dữ liệu bị thiếu- missing value ratio: loại bỏ các đặc trưng có tỷ lệ dữ liệu bị thiếu cao (không đáng tin cậy)
        + Độ tương hỗ- mutual information (độ đo MI ): tính toán độ tương hỗ giữa các đặc trưng và biến mục tiêu để xác định độ liên quan
        
        
PP wrapper (Wrapper method)
(thôi đi photo slide cho rồi)