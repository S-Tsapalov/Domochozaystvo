import psycopg2
import datetime

def proverka_zapasov_segodya_zavtra(cursor, connection):

    tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    today = datetime.date.today()

    cursor.execute("""
    SELECT culinarnaya_kniga.products  
    FROM culinarnaya_kniga
    JOIN plan_pitaniya 
    ON plan_pitaniya.recept = culinarnaya_kniga.id
    WHERE plan_pitaniya.date = %s OR plan_pitaniya.date = %s""",(today,tomorrow))

    result = cursor.fetchall()#список json'ов

    products = {}

    for ingredients in result:
        for product in ingredients.key():
            if product not in products:
                products[product] = ingredients.get(product)
            else:
                products[product] += ingredients.get(product)

    nedost_index = {}

    for product in products.keys():
        cursor.execute("""
            SELECT colichestvo  
            FROM zapas_productov
            WHERE product = %s """,(product,))

        colichestvo = cursor.fetchone()

        if colichestvo <= products[product]:
            nedost_index[product] = products[product]-colichestvo

    nedost_poroducts = {}

    for product in nedost_index.keys():
        cursor.execute("""
                    SELECT name_product  
                    FROM products
                    WHERE id = %s """, (product,))

        result = cursor.fetchone()
        nedost_poroducts[result] = nedost_index.get(product)

    return nedost_poroducts


