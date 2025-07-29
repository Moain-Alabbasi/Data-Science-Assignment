
import requests
import pandas as pd
from datetime import datetime

# استبدل بمفتاح News API الخاص بك
NEWS_API_KEY = "a1dc4db710a746868500d4a5e3c76cca"

# تعريف مصادر الأخبار واللغات
news_sources = {
    "english": ["bbc-news", "reuters", "cnn"],
    "arabic": ["al-jazeera-arabic", "argaam"]
}

all_news_data = []

for lang, sources in news_sources.items():
    for source_id in sources:
        print(f"جلب الأخبار من {source_id} ({lang})...")
        url = f"https://newsapi.org/v2/top-headlines?sources={source_id}&apiKey={NEWS_API_KEY}"
        response = requests.get(url)
        data = response.json()

        if data["status"] == "ok":
            for article in data["articles"]:
                all_news_data.append({
                    "المصدر": article["source"]["name"],
                    "العنوان": article["title"],
                    "تاريخ_النشر": article["publishedAt"]
                })
        else:
            print("خطأ في جلب الأخبار من {}. الاستجابة الكاملة: {}".format(source_id, data))

news_df = pd.DataFrame(all_news_data)

# تنظيف وتحويل البيانات (عمليات Pandas)
# تحويل عمود "تاريخ_النشر" إلى كائنات datetime
news_df["تاريخ_النشر"] = pd.to_datetime(news_df["تاريخ_النشر"], errors="coerce")

# استخراج التاريخ والوقت في أعمدة منفصلة
news_df["التاريخ"] = news_df["تاريخ_النشر"].dt.date
news_df["الوقت"] = news_df["تاريخ_النشر"].dt.time

# الفرز حسب المصدر وتاريخ النشر
news_df = news_df.sort_values(by=["المصدر", "تاريخ_النشر"]).reset_index(drop=True)

# أمثلة على استخدام دوال Pandas جديدة:
# 1. .drop_duplicates(): إزالة عناوين الأخبار المكررة
print("\nشكل DataFrame الأصلي:", news_df.shape)
news_df.drop_duplicates(subset=["العنوان"], inplace=True)
print("شكل DataFrame بعد إزالة التكرارات:", news_df.shape)

# 2. .value_counts(): عد مقالات الأخبار لكل مصدر
print("\nعدد مقالات الأخبار لكل مصدر:")
print(news_df["المصدر"].value_counts())

# 3. .nlargest(): الحصول على أحدث 5 مقالات
print("\nأحدث 5 مقالات:")
print(news_df.nlargest(5, "تاريخ_النشر"))

# تصدير إلى CSV
output_csv_path = "news_headlines.csv"
news_df.to_csv(output_csv_path, index=False)
print(f"\nتم حفظ عناوين الأخبار في {output_csv_path}")


