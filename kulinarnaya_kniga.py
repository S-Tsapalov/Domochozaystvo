# основная часть -Рецепт
{
  "id": "uuid или integer",
  "title": "Название рецепта",
  "description": "Краткое описание блюда",
  "ingredients": #[ /* массив объектов Ingredient */ ],
  "instructions": #[ /* массив шагов */ ],
  "prep_time": 20, #// в минутах
  "cook_time": 30,
  "total_time": 50,
  "servings": 4,
  "difficulty": "легкий", #// легкий, средний, сложный
  "category_id": "uuid", #// ссылка на категорию
  "tags": ["завтрак", "выпечка"], #// массив тегов
  "image_url": "/images/recipe.jpg",
  "source": "оригинальный источник, если есть",
  "rating": 4.5,
  "favorite": false,
  "created_date": "2023-10-01",
  "updated_date": "2023-10-05",
  "author_id": "uuid", #// если есть пользователи
  "visibility": "public" #// или private
}
# составная часть рецепта - Инградиенты
{
  "id": "uuid",
  "name": "мука пшеничная",
  "quantity": 200,
  "unit": "г", #// грамм, мл, шт., ст.л., ч.л., по вкусу, щепотка
  "note": "высший сорт" #// необязательное уточнение
}
# управление питанием - Категории рецептов
{
  "id": "uuid",
  "name": "Завтраки",
  "description": "Рецепты для утреннего приема пищи",
  "parent_id": "uuid или null", #// для вложенности (например, "Десерты" -> "Торты")
  "image_url": "/icons/breakfast.svg",
  "order": 1 #// для сортировки
}
# организация питания - Заметки (tag) - для быстрого ориентирования в рецептах
{
  "id": "uuid",
  "name": "вегетарианское",
  "type": "диета" #// опционально: диета, сезон, событие и т.д.
}
# План питания (meal_plans)
{
  "id": "uuid",
  "user_id": "uuid",
  "date": "2023-10-15",
  "meal_type": "ужин", #// завтрак, обед, ужин, перекус
  "recipe_id": "uuid",
  "servings": 2
}
# для нескольких человек - Едоки (users)
{
  "id": "uuid",
  "username": "chef_ivan",
  "email": "user@mail.com",
  "saved_recipes": ["recipe_id1", "recipe_id2"], #// избранное
  "meal_plans": #[ /* массив планов питания */ ],
  "shopping_lists": # [ /* массив списков покупок */ ]
}
# пополнение инградиентов - Покупки (shopping_lists)
{
  "id": "uuid",
  "user_id": "uuid",
  "name": "На неделю",
  "items": [
    {
      "ingredient_name": "мука",
      "quantity": 500,
      "unit": "г",
      "purchased": false,
      "recipe_ids": ["uuid1", "uuid2"] #// из каких рецептов добавлен
    }
  ],
  "created_date": "2023-10-10"
}

# Таблицы PoagreSQL: recipes, categories, tags, users, meal_plans, shopping_lists.

# Связующие таблицы: recipe_tags, recipe_categories, user_favorites.

# Ингредиенты можно хранить как JSON-поле в recipes или в отдельной таблице ingredients с ссылкой на рецепт.