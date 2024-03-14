$(document).ready(function () {
  $.ajax({
    url: "../JSON/ATMnumbers.json",
    dataType: "json",
    success: function (data) {
      for (var i = 0; i < data.length; i++) {
        let rowData;
        let cellValue;
        let firstcellValue;
        for (index in data[i]) {
          //   console.log(data[i][index]);
          if (isNaN(index)) {
            firstcellValue = data[i][index];
          } else {
            cellValue = data[i][index];
            rowData += "<td>" + cellValue + "</td>";
          }
        }
        rowData += "</tr>";
        let rowHTML =
          "<tr><th scope='row'>" + firstcellValue + "</th>" + rowData;
        $("#ATMnbr").append(rowHTML);
      }
    },
  });
  $.ajax({
    url: "../JSON/agenciesNumber.json",
    dataType: "json",
    success: function (data) {
      for (var i = 0; i < data.length; i++) {
        let rowData;
        let cellValue;
        let firstcellValue;
        for (index in data[i]) {
          //   console.log(data[i][index]);
          if (isNaN(index)) {
            if (index == "/") {
              rowData += "<td>/</td>";
            } else {
              firstcellValue = data[i][index];
            }
          } else {
            cellValue = data[i][index];
            rowData += "<td>" + cellValue + "</td>";
          }
        }
        rowData += "</tr>";
        let rowHTML =
          "<tr><th scope='row'>" + firstcellValue + "</th>" + rowData;
        $("#agenciesnbr").append(rowHTML);
      }
    },
  });
});

// ========================== jquery for navbar background ================
$(function () {
  $(document).scroll(function () {
    var $nav = $(".nav");
    $nav.toggleClass("scrolled", $(this).scrollTop() > $nav.height());
  });
});

// ============================== toggler menu =======================
var menu = document.getElementById("bar");
var items = document.getElementById("navbar");
items.style.left = "-360px";

menu.onclick = function () {
  if (items.style.left == "-360px") {
    items.style.left = "0";
  } else {
    items.style.left = "-360px";
  }
};
function closeModal() {
  $("#reserveModal").modal("hide");
}
if (document.getElementById("downloadLink")) {
  document
    .getElementById("downloadLink")
    .addEventListener("click", function () {
      // Perform any download-related actions here

      // Close the modal after a delay (you can adjust the delay as needed)
      setTimeout(closeModal, 1000);
    });
}
function selectPics(type) {
  let typemin = type.toLowerCase();
  let picforserviceID = 0;
  $(`#picsFor${type}`).change(function () {
    let selectedPictures = this.files;
    let selectedPicturesArr = $.map(selectedPictures, function (value, key) {
      return { key: key, value: value };
    });
    let picturesToAdd;
    if (selectedPictures.length > 0) {
      if (
        $(`#picsFor${type}Container`).children().length +
          selectedPictures.length >
        10
      ) {
        picturesToAdd = selectedPicturesArr.slice(
          0,
          10 - $(`#picsFor${type}Container`).children().length
        );
      } else {
        picturesToAdd = selectedPicturesArr;
      }
      picturesToAdd.forEach((picture) => {
        let file = picture.value;
        if (file.type && file.type.indexOf("image") !== -1) {
          var reader = new FileReader();
          reader.readAsDataURL(file);
          reader.onload = function (e) {
            picforserviceID++;
            let image = `<div id="picfor${typemin}-${picforserviceID}" class="col-4 square-container position-relative"
          >
          <img
            src="${e.target.result}"
            alt="${file.name}"
            class="square-image"
          />
          <svg
            class="remove-pic-svg position-absolute bg-light overflow-hidden rounded-circle"
            id="remove-picfor${typemin}-${picforserviceID}"
            data-idnbr="${picforserviceID}"
            data-role="remove-picfor${typemin}"
            xmlns="http://www.w3.org/2000/svg"
            viewBox="0 0 512 512"
          >
            <path
              d="M256 512A256 256 0 1 0 256 0a256 256 0 1 0 0 512zM175 175c9.4-9.4 24.6-9.4 33.9 0l47 47 47-47c9.4-9.4 24.6-9.4 33.9 0s9.4 24.6 0 33.9l-47 47 47 47c9.4 9.4 9.4 24.6 0 33.9s-24.6 9.4-33.9 0l-47-47-47 47c-9.4 9.4-24.6 9.4-33.9 0s-9.4-24.6 0-33.9l47-47-47-47c-9.4-9.4-9.4-24.6 0-33.9z"
            />
          </svg>
        </div>`;
            $(`#picsFor${type}Container`).append(image);
          };
        }
      });
    }
  });
}
selectPics("Service");
$("#picsForServiceContainer").on("DOMSubtreeModified", function () {
  refreshRemovepicforpost();
});
function refreshRemovepicforpost() {
  $('[data-role="remove-picforservice"]').each(function () {
    $(this).on("click", function () {
      $(`#picforservice-${$(this).attr("data-idnbr")}`).remove();
    });
  });
}
function previewRecipe() {
  $("#recipeInput").change(function () {
    let selectedPictures = this.files;
    let selectedPicturesArr = $.map(selectedPictures, function (value, key) {
      return { key: key, value: value };
    });
    let picturesToAdd;
    if (selectedPictures.length > 0) {
      picturesToAdd = selectedPicturesArr;
      picturesToAdd.forEach((picture) => {
        let file = picture.value;
        if (file.type && file.type.indexOf("image") !== -1) {
          var reader = new FileReader();
          reader.readAsDataURL(file);
          reader.onload = function (e) {
            let image = `<img class="w-100" src="${e.target.result}" alt="${file.name}" />`;
            $("#recipeOutput").append(image);
            $("#confirmPayment").prop("disabled", false);
          };
        }
      });
    }
  });
}
if ($("#recipeInput")) {
  previewRecipe();
}
