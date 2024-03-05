
def sort_data(data: dict):
    caption = (f"Happy Birthday 🥳 \n"
               f"I/F: {data['first_name']} {data['last_name']} \n"
               f"Tug'ilgan sanasi: {data['birth_date']} \n"
               f"Lavozimi: {data['position']}")
    sorted_data = {
        'image': data['image'],
        'caption': caption
    }
    return sorted_data
