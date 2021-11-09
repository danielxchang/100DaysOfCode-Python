import requests
import datetime as dt
import pandas

USERNAME = "danielchang"
TOKEN = "jdi398dhwkf873gdfk378"
CSV_FILE = "graphs.csv"
headers = {
    "X-USER-TOKEN": TOKEN
}

data = pandas.read_csv(CSV_FILE)
graphs = {
    row.graph_name: {
        "id": row.id,
        "unit": row.unit
    }
    for i, row in data.iterrows()
}
graph_names = list(graphs.keys())


pixela_endpoint = 'https://pixe.la/v1/users'
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"


def create_account():
    token = input("Enter own token (validation rule: [ -~]{8,128): ")
    username = input("Enter username: ")

    user_params = {
        "token": token,
        "username": username,
        "agreeTermsOfService": "yes",
        "notMinor": "yes"
    }

    response = requests.post(url=pixela_endpoint, json=user_params)
    print(response.text)


def create_graph():
    graph_id = input("Enter graph id (validation rule: ^[a-z][a-z0-9-]{1,16}): ")
    name = input("Enter graph name: ")
    unit = input("Enter unit of measurement (miles, pages, km, etc): ")
    q_type = input("Enter unit type ('float' or 'int'): ")
    color = input("Choose a color - 'shibafu' (green), 'momiji' (red), 'sora' (blue), 'ichou' (yellow), "
                  "'ajisai' (purple) and 'kuro' (black): ")

    graph_config = {
        "id": graph_id,
        "name": name,
        "unit": unit,
        "type": q_type,
        "color": color
    }

    if input(f"Enter 'y' to confirm the following configuration: {graph_config}: ").lower() == "y":
        response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
        print(response.text)
        if response.status_code == 200:
            new_df = pandas.DataFrame({
                "graph_name": [name],
                "id": [graph_id],
                "unit": [unit]
            })
            new_data = data.append(new_df, ignore_index=True)
            new_data.to_csv(CSV_FILE, index=False)


def delete_graph():
    graph_name = input(f"Pick a graph {graph_names}: ")
    delete_graph_endpoint = f"{graph_endpoint}/{graphs[graph_name]['id']}"
    response = requests.delete(url=delete_graph_endpoint, headers=headers)
    print(response.text)
    if response.status_code == 200:
        new_data = data.drop(data[data['graph_name'] == graph_name].index)
        new_data.to_csv(CSV_FILE, index=False)


def get_graph_url():
    graph_name = input(f"Pick a graph {graph_names}: ")
    get_graph_endpoint = f"{graph_endpoint}/{graphs[graph_name]['id']}.html"
    print(get_graph_endpoint)


def add_pixel():
    pixel_creation_endpoint, pixel_data = get_pixel_parameters()
    print(pixel_creation_endpoint)
    response = requests.post(url=pixel_creation_endpoint, headers=headers, json=pixel_data)
    print(response.text)


def update_pixel():
    pixel_update_endpoint, pixel_data = get_pixel_parameters("update")
    response = requests.put(url=f"{pixel_update_endpoint}", headers=headers, json=pixel_data)
    print(response.text)


def delete_pixel():
    pixel_delete_endpoint = get_pixel_parameters("delete")
    response = requests.delete(url=pixel_delete_endpoint, headers=headers)
    print(response.text)


def get_pixel_parameters(mode="add"):
    graph_name = input(f"Pick a graph {graph_names}: ")
    date = input("Enter 'today' or another date in yyyyMMdd format: ")
    formatted_date = dt.date.today().strftime("%Y%m%d") if date == "today" else date

    pixel_endpoint = f"{graph_endpoint}/{graphs[graph_name]['id']}"

    if mode != "add":
        pixel_endpoint = f"{pixel_endpoint}/{formatted_date}"
        if mode == "delete":
            return pixel_endpoint

    quantity = input(f"Enter quantity ({graphs[graph_name]['unit']}): ")

    pixel_data = {
        "date": formatted_date,
        "quantity": quantity
    }

    return pixel_endpoint, pixel_data


def habit_tracker():
    actions = {
        1: create_account,
        2: create_graph,
        3: delete_graph,
        4: get_graph_url,
        5: add_pixel,
        6: update_pixel,
        7: delete_pixel,
    }

    actions_list = [f"enter '{key}' to {action.__name__}" for key, action in actions.items()]
    action = int(input(f'Select one of the following actions below: \n{actions_list}\n'))
    if actions.get(action):
        actions[action]()
    else:
        print("No valid action entered.")


if __name__ == "__main__":
    habit_tracker()
