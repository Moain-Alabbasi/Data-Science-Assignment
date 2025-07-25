# أكواد المحاضرة الثانية: جمع البيانات ومعالجة البيانات المسبقة (نظري)

## Example 2.1 (صفحة 8): واجهات برمجة التطبيقات (APIs) وطلبات HTTP في بايثون
"""
شرح المثال:
يوضح كيفية استخدام مكتبة requests لإجراء طلبات HTTP إلى واجهات برمجة التطبيقات (APIs)
1. تحديد مفتاح API والمدينة المستهدفة
2. بناء رابط الطلب (URL) باستخدام معلمات البحث
3. إرسال طلب GET والحصول على الاستجابة
4. التحقق من نجاح الطلب (رمز الحالة 200)
5. تحويل البيانات إلى تنسيق JSON وعرضها
"""
import requests

# مثال على استدعاء API للحصول على بيانات الطقس
api_key = "your_api_key_here"  # استبدل هذا بمفتاح API الخاص بك
city = "London"
url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("خطأ في جلب البيانات")

# ---------------------------

## Example 2.2 (صفحة 10): كشط الويب (Web Scraping) في بايثون
"""
شرح المثال:
يوضح كيفية استخراج البيانات من صفحات الويب باستخدام مكتبتي requests و BeautifulSoup
1. إرسال طلب GET إلى عنوان URL المطلوب
2. تحليل محتوى HTML باستخدام BeautifulSoup
3. البحث عن عناصر محددة باستخدام الوسوم وخصائص CSS
4. استخراج النص من العناصر وعرض النتائج
"""
import requests
from bs4 import BeautifulSoup

url = "https://example.com"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')

    # البحث عن جميع عناوين الأخبار (مثال)
    # نفترض أن عناوين الأخبار موجودة داخل وسم <h2> مع فئة 'news-title'
    news_titles = soup.find_all('h2', class_='news-title')

    for title in news_titles:
        print(title.text)
else:
    print("خطأ في جلب صفحة الويب")

# ---------------------------

## Example 2.3 (صفحة 11): جمع البيانات من نماذج جوجل
"""
شرح المثال:
يوضح كيفية معالجة البيانات المجمعة من نماذج جوجل
1. تصدير الردود من نماذج جوجل كملف CSV
2. قراءة ملف CSV باستخدام مكتبة pandas
3. عرض البيانات الأولية لفهم هيكل البيانات
"""
import pandas as pd

# قراءة بيانات نماذج جوجل المصدرة كملف CSV
# يجب أن يكون ملف 'google_forms_responses.csv' موجودًا في نفس مجلد الكود أو تحديد المسار الكامل له.
df = pd.read_csv("google_forms_responses.csv")
print(df.head())  # عرض أول 5 صفوف من البيانات

# ---------------------------

## Example 2.4 (صفحة 12): مجموعات بيانات Kaggle
"""
شرح المثال:
يوضح كيفية استخدام مجموعات البيانات المتاحة على منصة Kaggle
1. تنزيل مجموعة البيانات المطلوبة من Kaggle
2. قراءة ملف البيانات باستخدام pandas
3. استكشاف البيانات الأساسية وعرض معلومات موجزة عنها
"""
import pandas as pd

# قراءة مجموعة بيانات من Kaggle (افترض أن الملف تم تنزيله)
# يجب أن يكون ملف 'kaggle_dataset.csv' موجودًا في نفس مجلد الكود أو تحديد المسار الكامل له.
df = pd.read_csv("kaggle_dataset.csv")
print("عرض أول 5 صفوف من البيانات:")
print(df.head())
print("\nمعلومات موجزة عن البيانات:")
print(df.info())

# ---------------------------

## Example 2.5 (صفحة 18): تنظيف البيانات - القيم المفقودة
"""
شرح المثال:
يوضح كيفية التعامل مع القيم المفقودة في البيانات
1. إنشاء بيانات عينة تحتوي على قيم مفقودة (NaN)
2. الكشف عن القيم المفقودة باستخدام isnull().sum()
3. معالجة القيم المفقودة بطريقتين:
   - حذف الصفوف التي تحتوي على قيم مفقودة (dropna)
   - ملء القيم المفقودة باستخدام المتوسط أو الوسيط
"""
import pandas as pd
import numpy as np

# إنشاء بيانات عينة تحتوي على قيم مفقودة
data = {
    'Name': ['Alice', 'Bob', 'Charlie', None, 'Eve'],
    'Age': [25, None, 35, 40, 28],
    'Salary': [50000, 60000, None, 90000, 55000]
}
df = pd.DataFrame(data)

print("DataFrame الأصلي:")
print(df)

# التحقق من القيم المفقودة في كل عمود
print("\nعدد القيم المفقودة في كل عمود:")
print(df.isnull().sum())

# إسقاط (حذف) الصفوف التي تحتوي على أي قيم مفقودة
df_cleaned = df.dropna()
print("\nDataFrame بعد إسقاط الصفوف ذات القيم المفقودة:")
print(df_cleaned)

# ملء القيم المفقودة
df_filled = df.fillna({
    'Name': 'Unknown',
    'Age': df['Age'].mean(),
    'Salary': df['Salary'].median()
})
print("\nDataFrame بعد ملء القيم المفقودة:")
print(df_filled)

# ---------------------------

## Example 2.6 (صفحة 19): دمج البيانات وتحويلها
"""
شرح المثال:
يوضح تقنيتين أساسيتين في معالجة البيانات:
1. دمج مجموعتي بيانات باستخدام عمود مشترك (ID)
2. تطبيع البيانات (Normalization) لتوحيد المقاييس بين الميزات المختلفة
"""
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# مثال على دمج البيانات - دمج مجموعتي بيانات
df1 = pd.DataFrame({
    'ID': [1, 2, 3, 4],
    'Name': ['Alice', 'Bob', 'Charlie', 'David']
})

df2 = pd.DataFrame({
    'ID': [1, 2, 3, 4],
    'Department': ['HR', 'IT', 'Finance', 'Marketing']
})

# دمج مجموعتي البيانات بناءً على عمود 'ID'
merged_df = pd.merge(df1, df2, on='ID')
print("DataFrame المدمج:")
print(merged_df)

# مثال على تحويل البيانات - التطبيع (Normalization)
data = pd.DataFrame({
    'Feature1': [10, 20, 30, 40, 50],
    'Feature2': [100, 200, 300, 400, 500]
})

scaler = MinMaxScaler()  # إنشاء كائن MinMaxScaler
normalized_data = scaler.fit_transform(data)  # تطبيق التطبيع
normalized_df = pd.DataFrame(normalized_data, columns=data.columns)

print("\nالبيانات الأصلية:")
print(data)
print("\nالبيانات المطبعة (Normalized):")
print(normalized_df)

# ---------------------------

## Example 2.7 (صفحة 21): اختيار الميزات وتقليل الأبعاد
"""
شرح المثال:
يوضح تقنيتين متقدمتين لتحسين جودة البيانات:
1. اختيار الميزات (Feature Selection): تحديد أهم الميزات باستخدام خوارزمية SelectKBest
2. تقليل الأبعاد (Dimensionality Reduction): استخدام PCA لضغط المعلومات في أبعاد أقل
"""
import pandas as pd
from sklearn.feature_selection import SelectKBest, f_classif
from sklearn.decomposition import PCA
import numpy as np

# إنشاء بيانات عينة (100 صف، 5 ميزات)
np.random.seed(42)
X = np.random.rand(100, 5)  # 5 ميزات (متغيرات مستقلة)
y = np.random.randint(0, 2, 100)  # متغير هدف ثنائي (0 أو 1)

print("الشكل الأصلي للبيانات (الصفوف، الأعمدة):", X.shape)

# اختيار أفضل 3 ميزات
selector = SelectKBest(score_func=f_classif, k=3)
X_selected = selector.fit_transform(X, y)
print("شكل الميزات المختارة:", X_selected.shape)

# تقليل الأبعاد إلى 3 مكونات رئيسية
pca = PCA(n_components=3)
X_pca = pca.fit_transform(X)
print("شكل البيانات بعد تقليل الأبعاد:", X_pca.shape)
print("نسبة التباين المفسر لكل مكون:", pca.explained_variance_ratio_)

# ---------------------------

## Example 2.8 (صفحة 23): تقسيم البيانات (Data Discretization)
"""
شرح المثال:
يوضح كيفية تحويل البيانات المستمرة إلى فئات (bins) بطريقتين:
1. التقسيم بعرض ثابت (Fixed-width binning): تقسيم البيانات إلى نطاقات متساوية
2. التقسيم بتردد متساوٍ (Equal frequency binning): تقسيم البيانات إلى مجموعات متساوية في الحجم
"""
import pandas as pd
import numpy as np

# إنشاء بيانات عينة مستمرة
data = pd.DataFrame({
    'Age': [22, 25, 35, 45, 55, 65, 75, 18, 30, 40]
})

print("بيانات العمر الأصلية:")
print(data['Age'])

# التقسيم بعرض ثابت
data['Age_Binned_Fixed'] = pd.cut(data['Age'], bins=3, labels=['Young', 'Middle', 'Old'])

# التقسيم بتردد متساوٍ
data['Age_Binned_Dynamic'] = pd.qcut(data['Age'], q=3, labels=['Low', 'Medium', 'High'])

print("\nبعد التقسيم إلى فئات:")
print(data)

# ---------------------------

## Example 2.9 (صفحة 24): مسار عمل كامل للمعالجة المسبقة للبيانات
"""
شرح المثال:
يوضح سير عمل متكامل لمعالجة البيانات يشمل:
1. التعامل مع القيم المفقودة (الملء بالمتوسط والوسيط)
2. ترميز المتغيرات النصية إلى رقمية
3. توحيد مقاييس البيانات (Feature Scaling)
4. تقسيم البيانات إلى مجموعات تدريب واختبار
"""
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split

# تحميل بيانات عينة
data = pd.DataFrame({
    'Age': [25, 30, np.nan, 40, 35],
    'Income': [50000, 60000, 70000, np.nan, 55000],
    'Education': ['Bachelor', 'Master', 'PhD', 'Bachelor', 'Master'],
    'Target': [0, 1, 1, 0, 1]  # متغير هدف ثنائي
})

print("البيانات الأصلية:")
print(data)

# الخطوة 1: التعامل مع القيم المفقودة
data['Age'].fillna(data['Age'].mean(), inplace=True)
data['Income'].fillna(data['Income'].median(), inplace=True)

# الخطوة 2: ترميز المتغيرات النصية
le = LabelEncoder()
data['Education_Encoded'] = le.fit_transform(data['Education'])

# الخطوة 3: توحيد مقاييس البيانات
scaler = StandardScaler()
features_to_scale = ['Age', 'Income']
data[features_to_scale] = scaler.fit_transform(data[features_to_scale])

# الخطوة 4: فصل الميزات والمتغير الهدف
X = data[['Age', 'Income', 'Education_Encoded']]
y = data['Target']

# الخطوة 5: تقسيم البيانات
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

print("\nالبيانات بعد المعالجة:")
print(data)
print("\nشكل مجموعة التدريب (الميزات):", X_train.shape)
print("شكل مجموعة الاختبار (الميزات):", X_test.shape)