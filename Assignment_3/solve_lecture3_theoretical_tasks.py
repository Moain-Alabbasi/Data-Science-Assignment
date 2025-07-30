import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# تحميل مجموعة بيانات تيتانيك
try:
    titanic_df = pd.read_csv("train.csv")
except FileNotFoundError:
    print("ملف train.csv غير موجود. يرجى التأكد من وجوده في نفس المسار.")
    exit()

# تنظيف البيانات: التعامل مع القيم المفقودة في عمود العمر
# يمكن استبدال القيم المفقودة بمتوسط العمر أو وسيطه
titanic_df["Age"].fillna(titanic_df["Age"].median(), inplace=True)

# إنشاء Box Plot لمقارنة أعمار الضحايا والناجين
plt.figure(figsize=(8, 6))
sns.boxplot(x="Survived", y="Age", data=titanic_df)
plt.title("مقارنة أعمار الناجين وغير الناجين في تيتانيك")
plt.xlabel("النجاة (0 = لم ينجُ، 1 = نجا)")
plt.ylabel("العمر")
plt.xticks([0, 1], ["لم ينجُ", "نجا"])
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.savefig("titanic_age_boxplot.png")
plt.show()

print("تم إنشاء Box Plot وحفظه باسم titanic_age_boxplot.png")



# إنشاء Pivot Table لمعدل البقاء على قيد الحياة حسب الطبقة والجنس
pivot_table = titanic_df.pivot_table(
    values="Survived",
    index="Pclass",  # الطبقة (1st, 2nd, 3rd)
    columns="Sex",   # الجنس (male, female)
    aggfunc="mean"   # حساب المتوسط (يمثل معدل البقاء على قيد الحياة)
)

print("\nPivot Table لمعدل البقاء على قيد الحياة حسب الطبقة والجنس:")
print(pivot_table)
