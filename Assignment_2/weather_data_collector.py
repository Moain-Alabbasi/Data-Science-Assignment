
import requests
import pandas as pd
from datetime import datetime, timedelta

# تعريف المدن وخطوط الطول والعرض الخاصة بها
cities = {
    'لندن': {'latitude': 51.5074, 'longitude': 0.1278},
    'نيويورك': {'latitude': 40.7128, 'longitude': -74.0060},
    'طوكيو': {'latitude': 35.6895, 'longitude': 139.6917},
    'دبي': {'latitude': 25.276987, 'longitude': 55.296249},
    'سيدني': {'latitude': -33.8688, 'longitude': 151.2093},
    'القاهرة': {'latitude': 30.0444, 'longitude': 31.2357},
    'ريو دي جانيرو': {'latitude': -22.9068, 'longitude': -43.1729},
    'موسكو': {'latitude': 55.7558, 'longitude': 37.6173},
    'بكين': {'latitude': 39.9042, 'longitude': 116.4074},
    'كيب تاون': {'latitude': -33.9249, 'longitude': 18.4241}
}

# تحديد النطاق الزمني لأسبوع واحد (اليوم وحتى 6 أيام ماضية)
end_date = datetime.now()
start_date = end_date - timedelta(days=6)

all_weather_data = []

for city_name, coords in cities.items():
    print(f"جلب البيانات لـ {city_name}...")
    url = (
        f"https://api.open-meteo.com/v1/forecast?latitude={coords['latitude']}&longitude={coords['longitude']}&hourly=temperature_2m,weather_code&daily=temperature_2m_max,temperature_2m_min,weather_code&timezone=auto&start_date={start_date.strftime('%Y-%m-%d')}&end_date={end_date.strftime('%Y-%m-%d')}"
    )
    response = requests.get(url)
    data = response.json()

    if 'daily' in data:
        for i in range(len(data['daily']['time'])):
            date = data['daily']['time'][i]
            temp_max = data['daily']['temperature_2m_max'][i]
            temp_min = data['daily']['temperature_2m_min'][i]
            weather_code = data['daily']['weather_code'][i]

            # ربط رمز الطقس بوصف أكثر تفصيلاً (مبسط للمثال)
            weather_description = "غير معروف"
            if weather_code == 0: weather_description = "سماء صافية"
            elif weather_code in [1, 2, 3]: weather_description = "غائم جزئياً، غائم كلياً، وغائم"
            elif weather_code in [45, 48]: weather_description = "ضباب وضباب صقيعي"
            elif weather_code in [51, 53, 55]: weather_description = "رذاذ"
            elif weather_code in [56, 57]: weather_description = "رذاذ متجمد"
            elif weather_code in [61, 63, 65]: weather_description = "مطر"
            elif weather_code in [66, 67]: weather_description = "مطر متجمد"
            elif weather_code in [71, 73, 75]: weather_description = "تساقط ثلوج"
            elif weather_code in [77]: weather_description = "حبيبات ثلجية"
            elif weather_code in [80, 81, 82]: weather_description = "زخات مطر"
            elif weather_code in [85, 86]: weather_description = "زخات ثلج"
            elif weather_code in [95]: weather_description = "عاصفة رعدية"
            elif weather_code in [96, 99]: weather_description = "عاصفة رعدية مع برد خفيف وكثيف"

            all_weather_data.append({
                'المدينة': city_name,
                'التاريخ': date,
                'درجة_الحرارة_العظمى_مئوية': temp_max,
                'درجة_الحرارة_الصغرى_مئوية': temp_min,
                'حالة_الطقس': weather_description
            })

weather_df = pd.DataFrame(all_weather_data)

# تنظيف وتحويل البيانات (أمثلة على عمليات Pandas)
# تحويل عمود 'التاريخ' إلى كائنات datetime
weather_df['التاريخ'] = pd.to_datetime(weather_df['التاريخ'])

# الفرز حسب المدينة والتاريخ
weather_df = weather_df.sort_values(by=['المدينة', 'التاريخ']).reset_index(drop=True)

# عرض بعض المعلومات حول DataFrame
print("\nمعلومات DataFrame:")
weather_df.info()

print("\nوصف DataFrame:")
print(weather_df.describe())

# مثال على استخدام دالة Pandas جديدة: .query()
print("\nالطقس في لندن بدرجة حرارة عظمى > 15 درجة مئوية:")
print(weather_df.query('المدينة == "لندن" and درجة_الحرارة_العظمى_مئوية > 15'))

# مثال على استخدام دالة Pandas جديدة: .groupby() و .agg()
print("\nمتوسط درجة الحرارة الصغرى/العظمى لكل مدينة:")
print(weather_df.groupby('المدينة').agg(متوسط_درجة_الحرارة_الصغرى=('درجة_الحرارة_الصغرى_مئوية', 'mean'), متوسط_درجة_الحرارة_العظمى=('درجة_الحرارة_العظمى_مئوية', 'mean')))

# تصدير إلى CSV
output_csv_path = 'weather_data.csv'
weather_df.to_csv(output_csv_path, index=False)
print(f"\nتم حفظ بيانات الطقس في {output_csv_path}")


'''
الوصف: تم تطوير هذا المثال لقراءة بيانات الطقس 
(درجة الحرارة الصغرى والكبرى وحالة الطقس)
 لعشر مدن مختلفة حول العالم، ولمدة أسبوع كامل (10 أوقات على مدار الأسبوع).
  تم تخزين هذه البيانات في Pandas DataFrame وتصديرها إلى ملف CSV.
'''