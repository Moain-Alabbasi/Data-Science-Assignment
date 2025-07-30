import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# تحميل البيانات
titanic = sns.load_dataset('titanic')

# تنظيف الأعمار بإزالة القيم الفارغة
titanic = titanic.dropna(subset=['age'])

# تحسين أسماء الفئات لعرض أوضح
titanic['survived'] = titanic['survived'].map({0: 'لم ينجُ', 1: 'نجا'})

# رسم Box Plot مع تلوين حسب الجنس
plt.figure(figsize=(10, 6))
sns.boxplot(x='survived', y='age', hue='sex', data=titanic)
plt.title('توزيع الأعمار حسب حالة النجاة والجنس')
plt.xlabel('حالة النجاة')
plt.ylabel('العمر')
plt.legend(title='الجنس')
plt.tight_layout()
plt.show()

# إنشاء جدول محوري وتحسين العرض
pivot = titanic.pivot_table(values='survived', index='sex', columns='class', aggfunc=lambda x: (x=='نجا').mean())
print("معدل النجاة حسب الجنس والدرجة:")
print(pivot.round(2))