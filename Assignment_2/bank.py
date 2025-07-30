
import pandas as pd
import numpy as np


csv_content = """
CustomerID,Age,Nationality,LoanAmount,LoanGuarantee,AccountType,TransactionAmount,TransactionType,Date
1,30,Egyptian,50000,Yes,Savings,10000,Deposit,01-01-2023
2,45,Saudi,120000,No,Current,5000,Withdrawal,01-01-2023
3,22,Egyptian,30000,Yes,Savings,2000,Transfer,02-01-2023
4,60,Kuwaiti,80000,No,Current,15000,Deposit,02-01-2023
5,35,Egyptian,70000,Yes,Savings,3000,Withdrawal,03-01-2023
6,28,Saudi,NaN,No,Current,NaN,Deposit,03-01-2023
7,50,Egyptian,90000,Yes,Savings,7000,Transfer,04-01-2023
8,150,Kuwaiti,100000,No,Current,20000,Deposit,04-01-2023
9,40,Egyptian,60000,Yes,Savings,4000,Withdrawal,05-01-2023
10,30,Egyptian,50000,Yes,Savings,10000,Deposit,01-01-2023
11,25,Syrian,40000,No,Current,2500,Transfer,05-01-2023
12,55,Jordanian,NaN,Yes,Savings,8000,Deposit,06-01-2023
13,33,Egyptian,65000,No,Current,3500,Withdrawal,06-01-2023
14,48,Saudi,110000,Yes,Savings,6000,Transfer,07-01-2023
15,29,Egyptian,55000,No,Current,NaN,Deposit,07-01-2023
"""

with open('bank_data.csv', 'w') as f:
    f.write(csv_content)


# 2. قراءة البيانات
df = pd.read_csv('bank_data.csv')
print("\nالبيانات الأصلية:")
print(df)
print("\nمعلومات عن البيانات الأصلية:")
print(df.info())

# 3. تنظيف البيانات
# أ. التعامل مع القيم المفقودة (NaN)
# استبدال القيم المفقودة في 'LoanAmount' بمتوسط العمود
df['LoanAmount'].fillna(df['LoanAmount'].mean(), inplace=True)
# استبدال القيم المفقودة في 'TransactionAmount' بمتوسط العمود
df['TransactionAmount'].fillna(df['TransactionAmount'].mean(), inplace=True)
print("\nالبيانات بعد معالجة القيم المفقودة:")
print(df)

# ب. إزالة التكرارات
df.drop_duplicates(inplace=True)
print("\nالبيانات بعد إزالة التكرارات:")
print(df)

# ج. تصحيح الأخطاء (مثال: عمر غير منطقي)
# استبدال الأعمار غير المنطقية (أكبر من 100) بمتوسط العمر
df.loc[df['Age'] > 100, 'Age'] = df['Age'].mean()
print("\nالبيانات بعد تصحيح الأعمار غير المنطقية:")
print(df)

# د. توحيد تنسيق الجنسية (مثال: 'Egyptian' و 'egyptian')
df['Nationality'] = df['Nationality'].str.capitalize()
print("\nالبيانات بعد توحيد تنسيق الجنسية:")
print(df)

# 4. تحويل البيانات
# أ. تحويل 'LoanGuarantee' إلى رقمي (Yes/No -> 1/0)
df['LoanGuarantee'] = df['LoanGuarantee'].map({'Yes': 1, 'No': 0})
print("\nالبيانات بعد تحويل 'LoanGuarantee':")
print(df)

# ب. تحويل 'AccountType' و 'TransactionType' باستخدام One-Hot Encoding
df = pd.get_dummies(df, columns=['AccountType', 'TransactionType'], drop_first=True)
print("\nالبيانات بعد One-Hot Encoding:")
print(df)

# ج. تحويل عمود التاريخ إلى تنسيق datetime وحساب ميزة جديدة (اليوم من الأسبوع)
df['Date'] = pd.to_datetime(df['Date'], format='%d-%m-%Y')
df['DayOfWeek'] = df['Date'].dt.day_name()
print("\nالبيانات بعد تحويل التاريخ وإضافة 'DayOfWeek':")
print(df)

# 5. تقليل البيانات (مثال: اختيار الميزات)
# في هذا المثال البسيط، لن نقوم بتقليل الأبعاد بشكل معقد، ولكن يمكننا اختيار أعمدة معينة.
# لنفترض أننا نريد التركيز على الأعمدة الرقمية الرئيسية للتحليل المالي.
financial_data = df[['LoanAmount', 'TransactionAmount', 'LoanGuarantee', 'Age']]
print("\nالبيانات المالية المختارة:")
print(financial_data)

# 6. تقطيع البيانات (مثال: تقطيع العمر إلى فئات)
# تقطيع العمر إلى فئات (صغير، متوسط، كبير)
bins = [0, 25, 45, 100]
labels = ['Young', 'Middle-aged', 'Senior']
df['AgeGroup'] = pd.cut(df['Age'], bins=bins, labels=labels, right=False)
print("\nالبيانات بعد تقطيع العمر إلى فئات:")
print(df[['Age', 'AgeGroup']])

# حفظ البيانات المعالجة إلى ملف CSV جديد
df.to_csv('processed_bank_data.csv', index=False)
print("\nتم حفظ البيانات المعالجة إلى processed_bank_data.csv")

