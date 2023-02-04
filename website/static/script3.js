const submitComment = document.getElementById("submit-comment");
const commentInput = document.getElementById("comment-input");
const commentsContainer = document.getElementById("comments-container");

// Initialize Firebase
var firebaseConfig = {
  apiKey: "AIzaSyCHOg3vkjosOhnUf0qij3ntdvLoQ8XoHr4",
  authDomain: "aquamainweb.firebaseapp.com",
  databaseURL: "https://aquamainweb-default-rtdb.firebaseio.com",
  projectId: "aquamainweb",
  storageBucket: "aquamainweb.appspot.com",
  messagingSenderId: "1015901461241",
  appId: "1:1015901461241:web:4bde306c1c60d47bc0a028",
  measurementId: "G-KM04TXPSJ2"
};
firebase.initializeApp(firebaseConfig);

// Get a reference to the Firebase Realtime Database
const database = firebase.database();

// Display comments from the database
database.ref("comments").on("value", function(snapshot) {
  commentsContainer.innerHTML = "";
  snapshot.forEach(function(childSnapshot) {
    let comment = childSnapshot.val().comment;
    let newComment = document.createElement("div");
    newComment.innerHTML = comment;
    commentsContainer.appendChild(newComment);
  });
});

submitComment.addEventListener("click", function() {
  let comment = commentInput.value;
  let newComment = document.createElement("div");
  newComment.innerHTML = comment;
  commentsContainer.appendChild(newComment);
  commentInput.value = "";

  // Save the new comment in the database
  database.ref("comments").push({
    comment: comment
  });
});
