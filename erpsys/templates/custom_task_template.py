<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Custom Task</title>
</head>
<body>
    <h1>
        Upload the text file.
    </h1>
    <form method="POST">
        {% csrf_token %}
        {{form.as_p}}
        <input type="submit" value="Submit">
    </form>
</body>
</html>