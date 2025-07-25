# أكواد المحاضرة الأولى: علم البيانات - NumPy (عملي)

## Example 1.1 (صفحة 5): إنشاء مصفوفة وطباعتها
"""
شرح المثال:
هذا المثال يوضح كيفية إنشاء مصفوفة بسيطة في بايثون بدون استخدام NumPy
حيث نقوم بإنشاء قائمة تحتوي على أرقام ثم طباعتها
"""
Array = [80, 85, 90, 95, 100, 105, 110, 115, 120, 125]
print(Array)

# ---------------------------

## Example 1.2 (صفحة 7): دالة max() - إيجاد القيمة القصوى
"""
شرح المثال:
هذا المثال يوضح كيفية استخدام دالة np.max() لإيجاد القيمة القصوى في مصفوفة NumPy
1. نقوم باستيراد مكتبة NumPy
2. ننشئ مصفوفة NumPy
3. نستخدم np.max() لحساب القيمة القصوى
4. نطبع النتائج
"""
import numpy as np

# إنشاء مصفوفة NumPy
array = np.array([10, 20, 30, 40, 50])

# إيجاد القيمة القصوى في المصفوفة
max_value = np.max(array)

print(f"المصفوفة هي: {array}")
print(f"القيمة القصوى في المصفوفة هي: {max_value}")

# ---------------------------

## Example 1.3 (صفحة 8): دالة min() - إيجاد القيمة الصغرى
"""
شرح المثال:
هذا المثال يوضح كيفية استخدام دالة np.min() لإيجاد القيمة الصغرى في مصفوفة NumPy
1. ننشئ مصفوفة NumPy
2. نستخدم np.min() لحساب القيمة الصغرى
3. نطبع النتائج
"""
import numpy as np

# إنشاء مصفوفة NumPy
array = np.array([10, 20, 30, 40, 50])

# إيجاد القيمة الصغرى في المصفوفة
min_value = np.min(array)

print(f"المصفوفة هي: {array}")
print(f"القيمة الصغرى في المصفوفة هي: {min_value}")

# ---------------------------

## Example 1.4 (صفحة 9): دالة mean() - حساب المتوسط
"""
شرح المثال:
هذا المثال يوضح كيفية استخدام دالة np.mean() لحساب متوسط قيم مصفوفة NumPy
1. ننشئ مصفوفة NumPy
2. نستخدم np.mean() لحساب المتوسط الحسابي
3. نطبع النتائج
"""
import numpy as np

# إنشاء مصفوفة NumPy
array = np.array([10, 20, 30, 40, 50])

# حساب متوسط المصفوفة
mean_value = np.mean(array)

print(f"المصفوفة هي: {array}")
print(f"متوسط المصفوفة هو: {mean_value}")

# ---------------------------

## Example 1.5 (صفحة 13): لماذا نستخدم NumPy؟ - مقارنة الأداء
"""
شرح المثال:
هذا المثال يوضح الفرق في الأداء بين استخدام NumPy وعدم استخدامها
1. نقارن بين حساب المسافة الإقليدية باستخدام بايثون العادية و NumPy
2. ننشئ نقطتين كبيرتين للمقارنة
3. نقيس وقت التنفيذ في كلتا الحالتين
4. النتيجة توضح أن NumPy أسرع بكثير مع البيانات الكبيرة
"""
import numpy as np
import time

# حساب المسافة الإقليدية بدون NumPy
def euclidean_distance_no_numpy(point1, point2):
    return sum([(p1 - p2)**2 for p1, p2 in zip(point1, point2)])**0.5

# حساب المسافة الإقليدية باستخدام NumPy
def euclidean_distance_numpy(point1, point2):
    return np.linalg.norm(np.array(point1) - np.array(point2))

# إنشاء نقاط كبيرة للاختبار
size = 10**6
point_a = [i for i in range(size)]
point_b = [i * 2 for i in range(size)]

# قياس الوقت بدون NumPy
start_time = time.time()
distance_no_numpy = euclidean_distance_no_numpy(point_a, point_b)
end_time = time.time()
print(f"المسافة بدون NumPy: {distance_no_numpy}")
print(f"الزمن بدون NumPy: {end_time - start_time:.6f} ثانية")

# قياس الوقت باستخدام NumPy
start_time = time.time()
distance_numpy = euclidean_distance_numpy(point_a, point_b)
end_time = time.time()
print(f"المسافة باستخدام NumPy: {distance_numpy}")
print(f"الزمن باستخدام NumPy: {end_time - start_time:.6f} ثانية")

# ---------------------------

## Example 1.6 (صفحة 15): تنظيف البيانات
"""
شرح المثال:
هذا المثال يوضح كيفية تنظيف البيانات في NumPy
1. ننشئ مصفوفة تحتوي على قيم مفقودة (NaN)
2. نحدد القيم المفقودة باستخدام np.isnan()
3. نستبدل القيم المفقودة بمتوسط القيم الموجودة (Mean Imputation)
4. بديلاً: نزيل القيم المفقودة تماماً
"""
import numpy as np

# إنشاء مصفوفة بقيم مفقودة (ممثلة بـ NaN)
data = np.array([10, 20, np.nan, 40, 50, np.nan, 70])

print(f"البيانات الأصلية: {data}")

# تحديد القيم المفقودة
missing_values = np.isnan(data)
print(f"قناع القيم المفقودة: {missing_values}")

# استبدال القيم المفقودة بمتوسط القيم الموجودة
mean_value = np.nanmean(data)
cleaned_data = np.nan_to_num(data, nan=mean_value)

print(f"البيانات النظيفة (استبدال بالمتوسط): {cleaned_data}")

# بديلاً: إزالة القيم المفقودة
removed_nan_data = data[~np.isnan(data)]
print(f"البيانات بعد إزالة القيم المفقودة: {removed_nan_data}")

# ---------------------------

## Example 1.7 (صفحة 16): التحليل الإحصائي
"""
شرح المثال:
هذا المثال يوضح كيفية إجراء تحليل إحصائي بسيط للبيانات المالية
1. نستخدم بيانات أسعار أسهم يومية
2. نحسب العوائد اليومية كنسبة مئوية
3. نحسب متوسط العوائد والانحراف المعياري
4. النتائج تعطي مؤشرات عن أداء السهم وتقلبه
"""
import numpy as np

# بيانات نموذجية (أسعار أسهم يومية)
stock_prices = np.array([100, 102, 98, 105, 103, 107, 101, 109, 106, 110])

# حساب العوائد اليومية
daily_returns = np.diff(stock_prices) / stock_prices[:-1] * 100

print(f"أسعار الأسهم: {stock_prices}")
print(f"العوائد اليومية (%): {daily_returns}")

# حساب متوسط العوائد والانحراف المعياري
mean_return = np.mean(daily_returns)
std_dev_return = np.std(daily_returns)

print(f"متوسط العائد اليومي: {mean_return:.2f}%")
print(f"الانحراف المعياري للعائد اليومي: {std_dev_return:.2f}%")

# ---------------------------

## Example 1.8 (صفحة 17): معالجة الصور
"""
شرح المثال:
هذا المثال يوضح كيفية استخدام NumPy في معالجة الصور
1. ننشئ صورة رمادية بسيطة كمصفوفة NumPy
2. نحول المصفوفة إلى صورة باستخدام مكتبة Pillow
3. نحفظ الصورة ثم نعيد تحميلها
4. نقوم بعملية عكس الألوان وحفظ الصورة المعدلة
"""
import numpy as np
from PIL import Image

# إنشاء صورة رمادية بسيطة كمصفوفة NumPy
# تمثل صورة 3x3 بكسلات
image_array = np.array([
    [50, 100, 150],
    [200, 250, 0],
    [120, 80, 180]
], dtype=np.uint8)

# تحويل مصفوفة NumPy إلى صورة
img = Image.fromarray(image_array)

# حفظ الصورة
img.save("photo.jpg")
print("تم حفظ الصورة كـ photo.jpg")

# تحميل الصورة وتحويلها لمصفوفة NumPy
loaded_img = Image.open("photo.jpg")
loaded_image_array = np.array(loaded_img)

print("\nالصورة المحملة كمصفوفة NumPy:")
print(loaded_image_array)

# عملية معالجة بسيطة (عكس الألوان)
inverted_image_array = 255 - loaded_image_array

# تحويل الصورة المعكوسة وحفظها
inverted_img = Image.fromarray(inverted_image_array)
inverted_img.save("inverted_photo.jpg")
print("تم حفظ الصورة المعكوسة كـ inverted_photo.jpg")

# ---------------------------

## Example 1.9 (صفحة 19): مقارنة بين NumPy والقوائم العادية
"""
شرح المثال:
هذا المثال يقارن الأداء بين NumPy والقوائم العادية في بايثون
1. ننشئ مجموعة بيانات كبيرة كقائمة عادية وكـمصفوفة NumPy
2. نقيس وقت حساب المتوسط في كلتا الحالتين
3. النتيجة توضح أن NumPy أسرع بكثير مع البيانات الكبيرة
"""
import numpy as np
import time

# قائمة عادية
_list = list(range(10**7))

# مصفوفة NumPy
numpy_array = np.arange(10**7)

# حساب المتوسط للقائمة العادية
start_time = time.time()
_mean = sum(_list) / len(_list)
end_time = time.time()
print(f"متوسط القائمة العادية: {_mean}")
print(f"الزمن المستغرق للقائمة العادية: {end_time - start_time:.6f} ثانية")

# حساب المتوسط لمصفوفة NumPy
start_time = time.time()
numpy_mean = np.mean(numpy_array)
end_time = time.time()
print(f"متوسط مصفوفة NumPy: {numpy_mean}")
print(f"الزمن المستغرق لمصفوفة NumPy: {end_time - start_time:.6f} ثانية")

# ---------------------------

## Example 1.10 (صفحة 20): مثال شامل لتحليل البيانات باستخدام NumPy
"""
شرح المثال:
هذا مثال شامل يوضح تطبيق عمليات متعددة على بيانات المستشعرات
1. نستخدم بيانات قراءات درجة حرارة لمدة 24 ساعة
2. نحسب الإحصائيات الأساسية (المتوسط، الوسيط، القيم القصوى، الانحراف المعياري)
3. نطبق تصفية للبيانات لاستخراج القراءات المرتفعة
4. نحول البيانات من مئوية إلى فهرنهايت
5. نعيد تشكيل البيانات إلى مصفوفة 4x6
6. نحسب متوسط درجة الحرارة لكل فترة (6 ساعات)
"""
import numpy as np

# محاكاة بيانات مستشعر (قراءات درجة الحرارة على مدار اليوم)
# 24 قراءة، واحدة لكل ساعة
sensor_data = np.array([
    22.5, 23.1, 22.8, 23.5, 24.0, 24.8, 25.5, 26.1, 27.0, 27.5, 28.0, 28.2,
    27.9, 27.0, 26.5, 25.8, 25.0, 24.5, 23.9, 23.0, 22.5, 22.0, 21.8, 21.5
])

print(f"بيانات المستشعر الأصلية: {sensor_data}")

# 1. الإحصائيات الأساسية
mean_temp = np.mean(sensor_data)
median_temp = np.median(sensor_data)
min_temp = np.min(sensor_data)
max_temp = np.max(sensor_data)
std_dev_temp = np.std(sensor_data)

print(f"\nمتوسط درجة الحرارة: {mean_temp:.2f}°C")
print(f"الوسيط الحرارى: {median_temp:.2f}°C")
print(f"أدنى درجة حرارة: {min_temp:.2f}°C")
print(f"أعلى درجة حرارة: {max_temp:.2f}°C")
print(f"الانحراف المعياري: {std_dev_temp:.2f}°C")

# 2. تصفية البيانات (قراءات فوق 25°C)
high_temp_readings = sensor_data[sensor_data > 25]
print(f"\nقراءات درجة الحرارة المرتفعة (>25°C): {high_temp_readings}")

# 3. تحويل البيانات (تحويل إلى فهرنهايت)
fahrenheit_data = (sensor_data * 9/5) + 32
print(f"\nدرجة الحرارة بالفهرنهايت: {fahrenheit_data}")

# 4. إعادة تشكيل البيانات (إلى مصفوفة 4x6 تمثل 4 فترات كل فترة 6 ساعات)
reshaped_data = sensor_data.reshape(4, 6)
print(f"\nبيانات معاد تشكيلها (مصفوفة 4x6):\n{reshaped_data}")

# 5. حساب متوسط درجة الحرارة لكل فترة (6 ساعات)
average_per_block = np.mean(reshaped_data, axis=1)

# طباعة متوسط درجة الحرارة لكل فترة
print("\nمتوسط درجة الحرارة لكل فترة (6 ساعات):")
for i, avg in enumerate(average_per_block, 1):
    print(f"الفترة {i}: {avg:.2f}°C")