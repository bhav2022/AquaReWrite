<?php
  $db = new mysqli("localhost", "username", "password", "database_name");

  if ($_POST) {
    if ($_POST["comment"]) {
      $comment = $db->real_escape_string($_POST["comment"]);
      $db->query("INSERT INTO comments (comment) VALUES ('$comment')");
    } elseif ($_POST["id"]) {
      $id = intval($_POST["id"]);
      $db->query("DELETE FROM comments WHERE id=$id");
    }
  } else {
    $result = $db->query("SELECT * FROM comments");
    while ($row = $result->fetch_assoc()) {
      echo '<div class="comment">';
      echo $row["comment"] . ' <button class="delete-button" data-id="' . $row["id"] . '">Delete</button>';
      echo '</div>';
    }
  }
?>
