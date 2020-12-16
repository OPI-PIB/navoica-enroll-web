/* Project specific Javascript goes here. */

function loadRegisterForm() {
  let countryInput = document.getElementById("id_country");
  let countyInput = document.getElementById("id_county");
  let voivodeshipInput = document.getElementById("id_voivodeship");
  let communeInput = document.getElementById("id_commune");
  let statusJobInput = document.getElementById("id_status");
  let jobProfessionInput = document.getElementById("id_profession");
  let workNameInput = document.getElementById("id_work_name");
  let peselInput = document.getElementById("id_pesel");
  let noPeselInput = document.getElementById("id_no_pesel");
  let submitBtn = document.getElementById("submit-id-submit");
  let hintWorkName = document.querySelector("#hint_id_work_name");

  let parentNoPesel = noPeselInput.parentNode;
  parentNoPesel.classList.add("align-self-center");
  let parentParentNopesel = parentNoPesel.parentNode;
  parentParentNopesel.classList.add("d-flex");
  parentParentNopesel.classList.add("h-100");
  parentParentNopesel.classList.add("mt-2");
  hintWorkName.classList.add("mb-5");
  hintWorkName.classList.add("mb-md-0");

  function enableInputsLocation() {
    countyInput.removeAttribute("disabled");
    communeInput.removeAttribute("disabled");
    voivodeshipInput.removeAttribute("disabled");
    document.querySelector("[for='id_county']").classList.remove("disabled");
    document
      .querySelector("[for='id_voivodeship']")
      .classList.remove("disabled");
    document.querySelector("[for='id_commune']").classList.remove("disabled");
  }

  function disableInputsLocation() {
    countyInput.setAttribute("disabled", "true");
    communeInput.setAttribute("disabled", "true");
    voivodeshipInput.setAttribute("disabled", "true");
    document.querySelector("[for='id_county']").classList.add("disabled");
    document.querySelector("[for='id_voivodeship']").classList.add("disabled");
    document.querySelector("[for='id_commune']").classList.add("disabled");
  }

  function changeVisibilityInputsLocation(value) {
    if (value.toLowerCase() === "polska" || value.toLowerCase() === "poland") {
      enableInputsLocation();
    } else {
      disableInputsLocation();
    }
  }

  function disableInputsStatusJob() {
    jobProfessionInput.setAttribute("disabled", "true");
    workNameInput.setAttribute("disabled", "true");
    document.querySelector("[for='id_profession']").classList.add("disabled");
    document.querySelector("[for='id_work_name']").classList.add("disabled");
  }

  function enableInputsStatusJob() {
    jobProfessionInput.removeAttribute("disabled");
    workNameInput.removeAttribute("disabled");
    document
      .querySelector("[for='id_profession']")
      .classList.remove("disabled");
    document.querySelector("[for='id_work_name']").classList.remove("disabled");
  }

  function changeVisibilityJob(value) {
    const hasJob = statusJobInput[1].value;
    if (value.toLowerCase() === hasJob.toLowerCase()) {
      enableInputsStatusJob();
    } else {
      disableInputsStatusJob();
    }
  }

  function checkPeselInput() {
    if (peselInput.value === "" && !noPeselInput.checked) {
      peselInput.setAttribute("required", "true");
    } else {
      peselInput.removeAttribute("required");
    }

    if (peselInput.value !== "") {
      noPeselInput.setAttribute("disabled", "true");
      document.querySelector("[for='id_no_pesel']").classList.add("disabled");
    } else {
      noPeselInput.removeAttribute("disabled");
      document
        .querySelector("[for='id_no_pesel']")
        .classList.remove("disabled");
    }

    if (noPeselInput.checked) {
      peselInput.setAttribute("disabled", "true");
      peselInput.removeAttribute("required");
      document.querySelector("[for='id_pesel']").classList.add("disabled");
    } else {
      peselInput.removeAttribute("disabled");
      peselInput.setAttribute("required", "true");
      document.querySelector("[for='id_pesel']").classList.remove("disabled");
    }
  }

  checkPeselInput();
  changeVisibilityInputsLocation(countryInput.value);
  changeVisibilityJob(statusJobInput.value);

  countryInput.addEventListener("input", function (e) {
    changeVisibilityInputsLocation(e.target.value);
  });

  statusJobInput.addEventListener("change", function () {
    changeVisibilityJob(this.value);
  });

  peselInput.addEventListener("input", function () {
    checkPeselInput();
  });

  noPeselInput.addEventListener("change", function () {
    checkPeselInput();
  });

  submitBtn.addEventListener("click", function () {
    checkPeselInput();
  });
}

document.addEventListener("DOMContentLoaded", loadRegisterForm);
