function signup() {
  $.ajax({
    url: "/accounts/signup/",
    type: "POST",
    data: {
      fname: $("#firstNameInputBasic").val(),
      lname: $("#lastNameInputBasic").val(),
      username: $("#usernameInputBasic").val(),
      password: $("#passwordInputBasic").val(),
      email: $("#emailInputBasic").val(),
      phone: $("#phoneInputBasic").val(),
      address: $("#addressInputBasic").val(),
      registerfreebtn: true,
    },
    headers: {
      "X-CSRFToken": $('input[name="csrfmiddlewaretoken"]').val(),
    },
    success: function (data) {
      console.log(data);
      if (data.code == 3) {
        window.location.href = "/";
      }
    },
    error: function (data) {
      console.error(data);
    },
  });
}
function signin() {
  $.ajax({
    url: "/accounts/signin/",
    type: "POST",
    data: {
      username: $("#usernameInputSignin").val(),
      password: $("#passwordInputSignin").val(),
      signinbtn: true,
    },
    headers: {
      "X-CSRFToken": $('input[name="csrfmiddlewaretoken"]').val(),
    },
    success: function (data) {
      console.log(data);
      if (data.code == 0) {
        window.location.href = "/";
      }
    },
    error: function (data) {
      console.error(data);
    },
  });
}
function confirmPayement() {
  let fileInput = $("#recipeInput");
  let recipeTypeInput = $("#recipeTypeInput");
  var formData = new FormData();
  formData.append("image", fileInput[0].files[0]);
  formData.append("type", recipeTypeInput.val());

  $.ajax({
    url: "/accounts/confirm_payement/",
    type: "POST",
    data: formData,
    processData: false, // Prevent jQuery from processing the data
    contentType: false, // Prevent jQuery from setting the content type
    headers: {
      "X-CSRFToken": $('input[name="csrfmiddlewaretoken"]').val(),
    },
    success: function (data) {
      console.log(data);
      if (data.code == 0) {
        $("#sentRecipeModal").modal("show");
      }
    },
    error: function (data) {
      console.error(data);
    },
  });
}
function sendConsulting() {
  let consultingMsg = $("#setConsultingArea").val();
  $.ajax({
    url: "/category/send_consulting/",
    type: "POST",
    data: { consulting: consultingMsg, sendConsultingBtn: true },
    headers: {
      "X-CSRFToken": $('input[name="csrfmiddlewaretoken"]').val(),
    },
    success: function (data) {
      console.log(data);
      if (data.code == 0) {
        $("#sendConsultingModal").modal("show");
      }
    },
    error: function (data) {
      console.error(data);
    },
  });
}
function hasSingleImageSelected(fileInput) {
  var files = fileInput[0].files; // Get the selected files
  if (files.length === 1) {
    var validImageTypes = ["image/jpeg", "image/png", "image/jpg"];
    if (validImageTypes.includes(files[0].type)) {
      return true; // Only one image file is selected
    }
  }
  return false; // Either no file selected or multiple files selected or not an image
}
function setReservation() {
  let data = {
    bank: $("#bankSelect").val(),
    branch: $("#branchSelect").val(),
    city: $("#citySelect").val(),
    dateTime: $("#datetimeInput").val(),
    barcodeData: `${$("#bankSelect").val()};${$("#branchSelect").val()};${$(
      "#citySelect"
    ).val()};${$("#datetimeInput").val()};`,
    setReservationBtn: true,
  };
  $.ajax({
    url: "/set_reservation/",
    type: "POST",
    data: data,
    dataType: "json",
    headers: {
      "X-CSRFToken": $('input[name="csrfmiddlewaretoken"]').val(),
    },
    success: function (data) {
      console.log(data);
      if (data.code == 0) {
        $("#reserveModal").modal("show");
        $("#downloadLink").attr("href", data.reservation);
        $("#barcodeImg").attr("src", data.reservation);
        console.log(data.reservation);
      }
    },
    error: function (xhr, errmsg, err) {
      alert("Error: " + errmsg);
    },
  });
}
function chooseBank() {
  let data = {
    chooseBankBtn: true,
  };
  $.ajax({
    url: "/choose_correct_bank/",
    type: "POST",
    data: data,
    dataType: "json",
    headers: {
      "X-CSRFToken": $('input[name="csrfmiddlewaretoken"]').val(),
    },
    success: function (data) {
      console.log(data);
      if (data.code == 0) {
        $("#chooseBankModal").modal("show");
        $("#bankChoosedBadge").text(data.bankChoosed);
      }
    },
    error: function (xhr, errmsg, err) {
      alert("Error: " + errmsg);
    },
  });
}
function setService() {
  let fileInput = $("#picsForService");
  let files = fileInput[0].files;
  let serviceDetails = $("#detailsTextarea");
  var formData = new FormData();
  for (var i = 0; i < files.length; i++) {
    formData.append("pictures", files[i]);
  }
  formData.append("description", serviceDetails.val());
  formData.append("setServiceBtn", true);

  $.ajax({
    url: "/set_service/",
    type: "POST",
    data: formData,
    processData: false, // Prevent jQuery from processing the data
    contentType: false, // Prevent jQuery from setting the content type
    headers: {
      "X-CSRFToken": $('input[name="csrfmiddlewaretoken"]').val(),
    },
    success: function (data) {
      console.log(data);
      if (data.code == 0) {
        $("#addServiceModal").modal("show");
      }
    },
    error: function (data) {
      console.error(data);
    },
  });
}
function sendMessage() {
  data = {
    full_name: $("#fullNameInput").val(),
    email: $("#emailInput").val(),
    phone: $("#phoneInput").val(),
    subject: $("#subjectInput").val(),
    message: $("#messageInput").val(),
  };
  $.ajax({
    url: "/accounts/message_us/",
    type: "POST",
    data: data,
    headers: {
      "X-CSRFToken": $('input[name="csrfmiddlewaretoken"]').val(),
    },
    success: function (data) {
      console.log(data);
      if (data.code == 0) {
        $("#messageSentModal").modal("show");
      }
    },
    error: function (data) {
      console.error(data);
    },
  });
}
$(document).ready(function () {
  $("#registerfreebtn").on("click", function (e) {
    signup();
  });
  $("#signinbtn").on("click", function (e) {
    signin();
  });
  $("#confirmPayment").on("click", function (e) {
    // check if the input #recipeInput has one image
    if (hasSingleImageSelected($("#recipeInput"))) {
      confirmPayement();
    }
  });
  $("#sendConsultingBtn").on("click", function (e) {
    sendConsulting();
  });
  $("#setReservationBtn").on("click", function (e) {
    setReservation();
  });
  $("#chooseBankBtn").on("click", function (e) {
    chooseBank();
  });
  $("#setServiceBtn").on("click", function (e) {
    setService();
  });
  $("#sentMessageBtn").on("click", function (e) {
    sendMessage();
  });
});
