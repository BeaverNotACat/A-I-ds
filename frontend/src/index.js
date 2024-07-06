var my_request = async function() {
  const response = await fetch(
    "http://192.168.1.102:8000/plan",
    {
        method: 'POST',
        body: JSON.stringify({
            "gender": "all",
            "age_from": 10,
            "age_to": 20,
            "income": "a",
            "avaliable_banners": 100

        }),
        headers: {
            'Content-Type': 'application/json',
            'Origin': 'http://127.0.0.1:8080/',
            'Access-Control-Allow-Origin': '*'
        }
  });
  const data = await response.json();
  console.log(data);
}


my_request();