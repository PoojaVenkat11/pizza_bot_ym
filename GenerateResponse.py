from flask import jsonify


def GenerateResponse(data, msg):
    response_data = {}
    data_list = []
    try:
        for i in data:
            temp = {}
            temp["ord_id"] = i[0]
            temp["piz_type"] = i[1]
            temp["piz_size"] = i[2]
            temp["cust_phn"]=i[3]
            temp["cust_addr"]=i[4]
            temp["status"]=i[5]
            data_list.append(temp)
            response_data["data"] = data_list

        response_data["msg"] = msg
        print(f"Respone data : {response_data}")
        return jsonify(response_data)
    except IndexError as e:
        print(e)
        return str(e)

