import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import shapiro, f_oneway

# 1. تحميل البيانات واكتشافها
print("\n--- الخطوة 1: تحميل البيانات واكتشافها ---")
try:
    sales_df = pd.read_csv("sales_data.csv")
    print("أول 5 صفوف من البيانات:")
    print(sales_df.head())
    print("\nمعلومات عن البيانات:")
    sales_df.info()
    print("\nالإحصائيات الوصفية:")
    print(sales_df.describe())
except FileNotFoundError:
    print("ملف sales_data.csv غير موجود. يرجى التأكد من وجوده في نفس المسار.")
    exit()

# 2. معالجة البيانات المفقودة
print("\n--- الخطوة 2: معالجة البيانات المفقودة ---")
print("القيم المفقودة قبل المعالجة:")
print(sales_df.isnull().sum())

# في هذا المثال، سنقوم بملء القيم المفقودة في الأعمدة العددية بالمتوسط
# والأعمدة الفئوية بالوضع (Mode)
for column in sales_df.columns:
    if sales_df[column].dtype == 'object':
        sales_df[column].fillna(sales_df[column].mode()[0], inplace=True)
    else:
        sales_df[column].fillna(sales_df[column].mean(), inplace=True)

print("\nالقيم المفقودة بعد المعالجة:")
print(sales_df.isnull().sum())

# تحويل عمود التاريخ إلى صيغة datetime
sales_df['Date'] = pd.to_datetime(sales_df['Date'])

# 3. إنشاء تصورات بيانية أساسية
print("\n--- الخطوة 3: إنشاء تصورات بيانية أساسية ---")

# Line Plot: تطور المبيعات عبر الزمن
plt.figure(figsize=(12, 6))
sales_df.set_index('Date')['Sales'].plot()
plt.title('تطور المبيعات عبر الزمن')
plt.xlabel('التاريخ')
plt.ylabel('المبيعات')
plt.grid(True)
plt.savefig('sales_time_series.png')
plt.show()

# Histogram: توزيع المبيعات
plt.figure(figsize=(8, 6))
sns.histplot(sales_df['Sales'], kde=True)
plt.title('توزيع المبيعات')
plt.xlabel('المبيعات')
plt.ylabel('التردد')
plt.savefig('sales_histogram.png')
plt.show()

# Bar Chart: المبيعات حسب المنطقة
plt.figure(figsize=(10, 6))
sales_by_region = sales_df.groupby('Region')['Sales'].sum().sort_values(ascending=False)
sns.barplot(x=sales_by_region.index, y=sales_by_region.values)
plt.title('إجمالي المبيعات حسب المنطقة')
plt.xlabel('المنطقة')
plt.ylabel('إجمالي المبيعات')
plt.savefig('sales_by_region_bar_chart.png')
plt.show()

# Scatter Plot: العلاقة بين عمر العميل والمبيعات
plt.figure(figsize=(10, 6))
sns.scatterplot(x='Customer_Age', y='Sales', data=sales_df)
plt.title('العلاقة بين عمر العميل والمبيعات')
plt.xlabel('عمر العميل')
plt.ylabel('المبيعات')
plt.savefig('age_sales_scatter_plot.png')
plt.show()

# 4. تحليل متقدم
print("\n--- الخطوة 4: تحليل متقدم ---")

# تحديد التوزيع (طبيعي أو منحرف) - اختبار شابيرو للمبيعات
stat, p = shapiro(sales_df['Sales'])
print(f'\nShapiro-Wilk Test for Sales: Statistics={stat:.3f}, p={p:.3f}')
if p > 0.05:
    print('البيانات تبدو وكأنها موزعة طبيعياً (لا يمكن رفض الفرضية الصفرية)')
else:
    print('البيانات لا تبدو وكأنها موزعة طبيعياً (رفض الفرضية الصفرية)')

# Box Plot للمبيعات حسب المنتج
plt.figure(figsize=(12, 7))
sns.boxplot(x='Product', y='Sales', data=sales_df)
plt.title('توزيع المبيعات حسب المنتج')
plt.xlabel('المنتج')
plt.ylabel('المبيعات')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.savefig('sales_by_product_boxplot.png')
plt.show()

# Heatmap لتحليل الارتباطات
# اختيار الأعمدة العددية فقط لحساب الارتباط
numeric_cols = sales_df.select_dtypes(include=['number'])
correlation_matrix = numeric_cols.corr()

plt.figure(figsize=(10, 8))
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('مصفوفة الارتباط بين المتغيرات العددية')
plt.savefig('correlation_heatmap.png')
plt.show()

# تحليل ANOVA (مثال: هل هناك فرق معنوي في المبيعات بين المناطق المختلفة؟)
# نحتاج إلى 3 مجموعات على الأقل لـ ANOVA
regions = sales_df['Region'].unique()
if len(regions) >= 2:
    # نأخذ أول منطقتين أو ثلاث للمثال
    group_data = [sales_df['Sales'][sales_df['Region'] == r] for r in regions[:3]]
    if len(group_data) >= 2:
        f_stat, p_val = f_oneway(*group_data)
        print(f'\nANOVA Test for Sales across Regions: F-statistic={f_stat:.3f}, p-value={p_val:.3f}')
        if p_val < 0.05:
            print('يوجد فرق معنوي في متوسط المبيعات بين المناطق.')
        else:
            print('لا يوجد فرق معنوي في متوسط المبيعات بين المناطق.')
    else:
        print("عدد المناطق غير كافٍ لإجراء اختبار ANOVA (يلزم منطقتين على الأقل).")
else:
    print("عدد المناطق غير كافٍ لإجراء اختبار ANOVA (يلزم منطقتين على الأقل).")

print("\nتم الانتهاء من التحليل الاستكشافي للبيانات.")