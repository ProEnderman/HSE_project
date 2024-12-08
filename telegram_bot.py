from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
import re
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error

df = pd.read_pickle("/Users/leonkul/projects/python/Session/df.pkl")

X = df[['Car Mileage', 'Year of Production', 'Transmission_rating', 
        'Engine Volume', 'Car Tier_rating', 'Specialness', 
        'Fuel Type_rating', 'Drivetrain_rating']]
y = df['Car Price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))

def predict_car_price(features):
    features_array = features.values if isinstance(features, pd.DataFrame) else np.array(features).reshape(1, -1)
    return model.predict(features_array)[0]


# Функция для предсказания цены автомобиля (здесь замените на вашу реализацию)

# Основной обработчик сообщений
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_data = context.user_data
    
    if 'step' not in chat_data:
        chat_data['step'] = 0
    if 'stats' not in chat_data:
        chat_data['stats'] = []

    step = chat_data['step']

    # Обработка каждого шага
    if step == 0:
        await update.message.reply_text("Enter Car Mileage:")
    elif step == 1:
        chat_data['stats'].append(float(update.message.text))
        await update.message.reply_text("Enter Year of Production:")
    elif step == 2:
        chat_data['stats'].append(float(update.message.text))
        await update.message.reply_text("Enter your transmission type:")
    elif step == 3:
        transmission_input = update.message.text
        transmission_rating = re.sub(r'(\d+)-Speed.*', r'\1', transmission_input)
        transmission_rating = re.sub(r'(\d+)-Spd.*', r'\1', transmission_rating)
        transmission_rating = re.sub(r'Automatic', '6', transmission_rating)
        transmission_rating = transmission_rating if re.match(r'^\d+$', transmission_rating) else '4'
        chat_data['stats'].append(int(transmission_rating))
        await update.message.reply_text("Enter the volume of your car's engine:")
    elif step == 4:
        chat_data['stats'].append(float(update.message.text))
        await update.message.reply_text("Enter the Car Brand:")
    elif step == 5:
        car_brand = update.message.text
        if car_brand in ['Ferrari', 'Lamborghini', 'McLaren', 'Bentley','Porsche','Rolls-Royce','Aston']:
            chat_data['stats'].append(10)
        elif car_brand in ['BMW', 'Mercedes-Benz', 'Audi','Rivian','Lotus','Maserati']:
            chat_data['stats'].append(9)
        elif car_brand in ['Volvo', 'Chevrolet', 'Cadillac', 'Land', 'Tesla','Jaguar', 'INFINITI','RAM','Lincoln','Nissan']:
            chat_data['stats'].append(6)
        elif car_brand in ['Ford', 'Mazda','Genesis','Toyota','GMC','Jeep','Acura','Lexus','Dodge','Alfa']:
            chat_data['stats'].append(4)
        elif car_brand in [ 'Buick', 'Chrysler', 'MINI', 'Mitsubishi', 'Scion', 'Subaru','Hyundai','Kia','Honda','Volkswagen']:
            chat_data['stats'].append(2)
        else:
            chat_data['stats'].append(5)
        await update.message.reply_text("Enter the full car name:")
    elif step == 6:
        car_name = update.message.text.split()
        special_name_keywords = ['Premium', 'Luxury', 'Sport', 'Grand', 'Edition', 'Turbo', 'Hybrid', 'Electric', 'Wagon', 'Limited','Touring','Ti']
        special_engine_keywords = ['Supercharged', 'Twin Turbo', 'Turbo Diesel','Turbocharged']
        specialness = 1 if set(car_name).intersection(special_name_keywords) else 0
        chat_data['stats'].append(specialness)
        await update.message.reply_text("Enter the Fuel Type of your car:")
    elif step == 7:
        fuel_type = update.message.text
        fuel_rating = {'Gasoline': 6, 'Diesel': 9, 'Electric': 8, 'E85 Flex Fuel': 3, 'Hybrid': 7, 'Flexible Fuel': 5}.get(fuel_type, 4)
        chat_data['stats'].append(fuel_rating)
        await update.message.reply_text("Enter the Drivetrain of your car (e.g., AWD, FWD, RWD):")
    elif step == 8:
        drivetrain = update.message.text
        drivetrain_rating = {'AWD': 8, '4WD': 9, 'FWD': 5, 'RWD': 6}.get(drivetrain, 4)
        chat_data['stats'].append(drivetrain_rating)

        # Предсказание цены
        stats = chat_data['stats']
        result = predict_car_price(stats)
        await update.message.reply_text(f"Result: {result}$. To try again write /restart")
        chat_data.clear()
        return

    chat_data['step'] += 1

# Команда /start
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Welcome to Car Price Predictor Bot! Let's start. Write anything to continue")
    context.user_data.clear()
    context.user_data['step'] = 0

async def restart_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Let's start over! Write anything to continue")
    context.user_data.clear()
    context.user_data['step'] = 0
    
# Настройка бота
def main():
    app = ApplicationBuilder().token("7691617195:AAGSXx7u7H8aeXMY5mjEe9ecj8dK_JIf3XA").build()

    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("restart", restart_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    app.run_polling()

if __name__ == "__main__":
    main()