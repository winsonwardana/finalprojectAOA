<?php
$servername = "localhost";
$username = "root";
$password = "";
$dbname = "finalproject";

// Create connection
$conn = new mysqli($servername, $username,$password,$dbname);
// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
if(isset($_POST['submit'])){
  $fullName = $_POST['fullName'];
  $dob = $_POST['dob'];
  $gender = $_POST['gender'];
  $address = $_POST['address'];
  $contact = $_POST['contact'];
  $age = $_POST['age'];
  $parents_name = $_POST['parents_name'];

  $sql = "INSERT INTO customer (name,dob, gender,address,contact,age,parents_name) VALUES ('$fullName','$dob','$gender','$address','$contact','$age','$parents_name')";
  if ($conn->query($sql) === TRUE) {
    echo "New record created successfully";
  } else {
    echo "Error: " . $sql . "<br>" . $conn->error;
    }

}



$conn->close();
?>
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <meta http-equiv="X-UA-Compatible" content="ie=edge" />
    <link href="form.css" rel="stylesheet" type="text/css" />
    <title>Forms with Tables</title>
    <link
      rel="stylesheet"
      href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css"
      integrity="sha384-ggOyR0iXCbMQv3Xipma34MD+dH/1fQ784/j6cY/iJTQUOhcWr7x9JvoRxT2MZw1T"
      crossorigin="anonymous"
    />
    <script
      src="https://code.jquery.com/jquery-3.3.1.slim.min.js"
      integrity="sha384-q8i/X+965DzO0rT7abK41JStQIAqVgRVzpbzo5smXKp4YfRvH+8abtTE1Pi6jizo"
      crossorigin="anonymous"
    ></script>
    <script
      src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"
      integrity="sha384-UO2eT0CpHqdSJQ6hJty5KVphtPhzWj9WO1clHTMGa3JDZwrnQq4sF86dIHNDz0W1"
      crossorigin="anonymous"
    ></script>
    <script
      src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"
      integrity="sha384-JjSmVgyd0p3pXB1rRibZUAYoIIy6OrQ6VrjIEaFf/nJGzIxFDsf4x0xIM+B07jRM"
      crossorigin="anonymous"
    ></script>
  </head>

  <body>
    <!-- Left Content -->
    <div class="split left">
      <div>
        <img
          src="school.jpg"
          alt="Avatar woman"
          style="width: 100%; margin-top:100px"
        />
      </div>
    </div>
    <!-- Right Content -->
    <div class="split right">
      <div style="padding: 20px;">
        <form method="post">
          <div class="form-group">
            <label for="exampleInputEmail1">Full Name</label>
            <input
              type="text"
              class="form-control"
              id="fullName"
              name="fullName"
              aria-describedby="emailHelp"
              placeholder="Full Name"
            />
          </div>
          <div class="form-group">
            <label for="exampleInputEmail1">Birthdate</label>
            <input
              class="form-control"
              type="date"
              name="dob"
              value="2011-08-19"
              id="Birthdate"
            />
          </div>
          <div class="form-group">
            <label for="exampleInputEmail1">Age</label>
            <input
              type="text"
              name="age"
              class="form-control"
              id="age"
              aria-describedby="emailHelp"
              placeholder="Age"
            />
          </div>
          <div class="form-group">
            <label for="exampleInputEmail1">Address</label>
            <input
              type="text"
              name="address"
              class="form-control"
              id="address"
              aria-describedby="emailHelp"
              placeholder="Address"
            />
            <small id="emailHelp" class="form-text text-muted"
              >We'll never share your address with anyone else.</small
            >
          </div>
          <div class="form-group">
            <label for="exampleInputPassword1">Contact Number</label>
            <input
              type="text"
              name="contact"
              class="form-control"
              id="parentsName"
              placeholder="Contact Number"
            />
          </div>
          <div class="form-group">
            <label for="exampleInputPassword1">Parent's Name</label>
            <input
              type="text"
              name="parents_name"
              class="form-control"
              id="parentsName"
              placeholder="Parents Name"
            />
          </div>
          <div class="form-group">
            <label for="exampleInputPassword1">Gender</label>
            <select name="gender" class="form-control">
              <option>Male</option>
              <option>Female</option>
            </select>
            <!-- Submit Button -->
          </div>
          <input type="submit" name="submit" value="Submit">
          <!-- <button type="submit" name="submit" class="btn btn-primary">Submit</button> -->
        </form>
      </div>
    </div>
  </body>
</html>
