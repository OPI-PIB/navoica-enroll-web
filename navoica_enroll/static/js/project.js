/* Project specific Javascript goes here. */

function loadRegisterForm() {
    let countryInput = document.getElementById("id_country");
    let countyInput = document.getElementById("id_county");
    let voivodeshipInput = document.getElementById("id_voivodeship");
    let communeInput = document.getElementById("id_commune");
    let statusJobInput = document.getElementById("id_status");
    let statusJobInfoInput = document.getElementById("id_status_info");
    let nationalityInput = document.getElementById("id_nationality");

    let jobProfessionInput = document.getElementById("id_profession");
    let workNameInput = document.getElementById("id_work_name");
    let peselInput = document.getElementById("id_pesel");
    let noPeselInput = document.getElementById("id_no_pesel");
    let submitBtn = document.getElementById("submit-id-submit");
    let hintWorkName = document.querySelector("#hint_id_work_name");
    let alert = document.querySelector(".js-show-register-alert");

    let parentNoPesel = noPeselInput.parentNode;
    parentNoPesel.classList.add("align-self-center");
    let parentParentNopesel = parentNoPesel.parentNode;
    parentParentNopesel.classList.add("d-flex");

    if (hintWorkName) {
        hintWorkName.classList.add("mb-5");
        hintWorkName.classList.add("mb-md-0");
    }

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

    function showAlertOnSubmit() {
        alert.classList.remove("d-none");
    }

    function hideAlertOnSubmit() {
        alert.classList.add("d-none");
    }

    const form = document.querySelector(".js-register-form form");
    let fieldContainers = document.querySelectorAll("[id^=div_id_]");
    const fieldArray = Array.from(fieldContainers);
    fieldArray.forEach(function (input) {
        let span = document.createElement("span");
        input.appendChild(span).classList.add("error-message");
        input.querySelector(".error-message").setAttribute("aria-atomic", "true");
        input
            .querySelector(".error-message")
            .setAttribute("aria-live", "assertive");
    });

    let inputs = document.querySelectorAll("[id^=id_]");

    const inputsArray = Array.from(inputs);
    inputsArray.forEach(function (input) {
        input.classList.add("js-field");
    });

    const fields = document.querySelectorAll(".js-field");

  const validation = {
    first_name: {
        pattern: /^(.*){1,100}$/i,
        isValid: false,
        isRequired: true,
        message: function (validationTranslates) {
            return validationTranslates.error_message_100_char_required;
        },
    },
    last_name: {
        pattern: /^(.*){1,100}$/i,
        isValid: false,
        isRequired: true,
        message: function (validationTranslates) {
            return validationTranslates.error_message_100_char_required;
        },
    },
    pesel: {
      pattern: /^[0-9]{11}$/,
      isValid: false,
      isRequired: true,
      message: function (validationTranslates) {
        return validationTranslates.error_message_pesel;
      },
    },
    no_pesel: {
      isValid: false,
      isRequired: true,
      validateFn: function (el) {
        if (peselInput.value) {
          removeErrorField(el);
          clearErrorMessage(el);
        } else {
          if (!el.checked || isFieldWithSpacesOnly(el)) {
            setErrorMessage(validationTranslates.error_message_required, el);
          } else {
            removeErrorField(el);
            clearErrorMessage(el);
            removeErrorField(peselInput);
            clearErrorMessage(peselInput);
          }
        }
      },
    },
    gender: {
      isValid: false,
      isRequired: true,
      validateFn: function (el) {
        if (!el.value) {
          setErrorMessage(validationTranslates.error_message_required, el);
        } else {
          removeErrorField(el);
          clearErrorMessage(el);
        }
      },
    },
    age: {
      pattern: /(?:\b|-)([1-9]{1,2}[0]?|100)\b/,
      isValid: false,
      isRequired: true,
      message: function (validationTranslates) {
        return validationTranslates.error_message_age;
      },
    },
    education: {
      isValid: false,
      isRequired: true,
      validateFn: function (el) {
        if (!el.value) {
          setErrorMessage(validationTranslates.error_message_required, el);
        } else {
          removeErrorField(el);
          clearErrorMessage(el);
        }
      },
    },
    phone: {
        pattern: /^(\(?\+?[0-9]*\)?)?[0-9\- \(\)]{8,30}$/,
        isValid: false,
        isRequired: true,
        message: function (validationTranslates, el) {
            if (!/^(\(?\+?[0-9]*\)?)?[0-9\- \(\)]{8,30}$/.test(el.value)) {
                return (
                    validationTranslates && validationTranslates.error_message_phone
                );
            } else if (el.value && el.value.length > 30) {
                return (
                    validationTranslates &&
                    validationTranslates.error_message_30_char_required
                );
            }
      },
    },
    email: {
      pattern: /^(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])$/,
      isValid: false,
      isRequired: true,
      message: function (validationTranslates) {
        return validationTranslates.error_message_email;
      },
    },
    street: {
        pattern: /^(.*){1,30}$/i,
        isValid: false,
        isRequired: true,
        message: function (validationTranslates) {
            return validationTranslates.error_message_300_char_required;
        },
    },
    street_no: {
      pattern: /^([a-zA-Z0-9]{1,10})*(\S+)$/,
      isValid: false,
      isRequired: true,
      message: function (validationTranslates) {
        return validationTranslates.error_message_10_char_required;
      },
    },
    street_building_no: {
      pattern: /^([a-zA-Z0-9]{1,10})*(\S+)$/,
      isValid: false,
      isRequired: false,
      message: function (validationTranslates) {
        return validationTranslates.error_message_10_char_required;
      },
    },
    postal_code: {
      pattern: /^[a-z0-9][a-z0-9\- ]{0,10}[a-z0-9]$/i,
      isValid: false,
      isRequired: true,
      message: function (validationTranslates) {
        return validationTranslates.error_message_12_char_required;
      },
    },
    city: {
        pattern: /^(.*){1,30}$/i,
        isValid: false,
        isRequired: true,
        message: function (validationTranslates) {
            return validationTranslates.error_message_30_char_required;
        },
    },
    country: {
        pattern: /^(.*){1,30}$/i,
        isValid: false,
        isRequired: true,
        message: function (validationTranslates) {
            return validationTranslates.error_message_30_char_required;
        },
    },
    voivodeship: {
      isValid: false,
      isRequired: true,
      validateFn: function (el) {
        if (!el.value) {
          setErrorMessage(validationTranslates.error_message_required, el);
        } else {
          removeErrorField(el);
          clearErrorMessage(el);
        }
      },
    },
    county: {
      isValid: false,
      isRequired: true,
      validateFn: function (el) {
        if (!el.value) {
          setErrorMessage(validationTranslates.error_message_required, el);
        } else {
          removeErrorField(el);
          clearErrorMessage(el);
        }
      },
    },
    commune: {
      isValid: false,
      isRequired: true,
      validateFn: function (el) {
        if (!el.value || isFieldWithSpacesOnly(el)) {
          setErrorMessage(validationTranslates.error_message_required, el);
        } else if (
          !/^(.*){1,30}$/.test(
              el.value
          )
        ) {
          setErrorField(el);
          setErrorMessage(
            validationTranslates.error_message_30_char_required,
            el
          );
        } else {
          removeErrorField(el);
          clearErrorMessage(el);
        }
      },
    },
    status: {
      isValid: false,
      isRequired: true,
      validateFn: function (el) {
        if (!el.value) {
          setErrorMessage(validationTranslates.error_message_required, el);
        } else {
          removeErrorField(el);
          clearErrorMessage(el);
        }
      },
    },
    profession: {
      isValid: false,
      isRequired: true,
      validateFn: function (el) {
        if (!el.value) {
          setErrorMessage(validationTranslates.error_message_required, el);
        } else {
          removeErrorField(el);
          clearErrorMessage(el);
        }
      },
    },
    work_name: {
      isValid: false,
      isRequired: true,
      validateFn: function (el) {
        if (!el.value || isFieldWithSpacesOnly(el)) {
          setErrorMessage(validationTranslates.error_message_required, el);
        } else if (
            !/^(.*){1,30}$/.test(
                el.value
            )
        ) {
          setErrorField(el);
          setErrorMessage(
            validationTranslates.error_message_1000_char_required,
            el
          );
        } else {
          removeErrorField(el);
          clearErrorMessage(el);
        }
      },
    },
    origin: {
      isValid: false,
      isRequired: true,
      validateFn: function (el) {
        validateRadioField(el, "[id^=id_origin]");
      },
    },
    homeless: {
      isValid: false,
      isRequired: true,
      validateFn: function (el) {
        validateRadioField(el, "[id^=id_homeless]");
      },
    },
    disabled_person: {
      isValid: false,
      isRequired: true,
      validateFn: function (el) {
        validateRadioField(el, "[id^=id_disabled_person]");
      },
    },
    social_disadvantage: {
      isValid: false,
      isRequired: true,
      validateFn: function (el) {
        validateRadioField(el, "[id^=id_social_disadvantage]");
      },
    },
    statement1: {
      isValid: false,
      isRequired: true,
      validateFn: function (el) {
        if (!el.checked) {
          setErrorMessage(
            validationTranslates.error_message_accept_field_required,
            el
          );
        } else {
          removeErrorField(el);
          clearErrorMessage(el);
        }
      },
    },
    statement2: {
      isValid: false,
      isRequired: true,
      validateFn: function (el) {
        if (!el.checked) {
          setErrorMessage(
            validationTranslates.error_message_approve_field_required,
            el
          );
        } else {
          removeErrorField(el);
          clearErrorMessage(el);
        }
      },
    },
  };

    function setErrorMessage(msg, el) {
        const errorElem = document.querySelector("#div_id_" + el.name);
        const errorElemMsg = errorElem && errorElem.querySelector(".error-message");
        errorElemMsg.textContent = msg;
    }

    function setErrorField(el) {
        el.setAttribute("aria-invalid", true);
        el.classList.add("error-field");
        if (validation) {
            validation[el.name].isValid = false;
        }
    }

    function removeErrorField(el) {
        el.removeAttribute("aria-invalid");
        el.classList.remove("error-field");
        if (validation) {
            validation[el.name].isValid = true;
        }
        let errorBackend = el.nextElementSibling;
        if (errorBackend && errorBackend.classList.contains("invalid-feedback")) {
            el.classList.remove("is-invalid");
            errorBackend.remove();
        }
    }

    function clearErrorMessage(el) {
        const errorElem = document.querySelector("#div_id_" + el.name);
        errorElem.querySelector(".error-message").textContent = "";
    }

    function validateRadioField(el, selectorNameStr) {
        let radioElems = document.querySelectorAll(selectorNameStr);

        let isCheckedRadio = Array.from(radioElems).some(function (radio) {
            return radio.checked;
        });

        if (!isCheckedRadio) {
            setErrorMessage(validationTranslates.error_message_radio_field, el);
            Array.from(radioElems).forEach(function (radio) {
                setErrorField(radio);
            });
        } else {
            Array.from(radioElems).forEach(function (radio) {
                removeErrorField(radio);
            });
            clearErrorMessage(el);
        }
    }

    function isFieldWithSpacesOnly(el) {
        return /^ *$/.test(el.value);
    }

    function validateForm(target) {
        if (target.value === "" || isFieldWithSpacesOnly(target)) {
            if (validation && validation[target.name].isRequired) {
                setErrorField(target);
                setErrorMessage(validationTranslates.error_message_required, target);
            }

            let hintElem = target.nextElementSibling;
            if (hintElem && hintElem.classList.contains("text-muted")) {
                hintElem.classList.add("d-none");
            }
        } else {
            if (
                validation[target.name] &&
                validation[target.name].hasOwnProperty("pattern")
            ) {
                if (!validation[target.name].pattern.test(target.value)) {
                    setErrorField(target);
                    setErrorMessage(
                        validation[target.name].message(validationTranslates, target),
                        target
                    );
                    let hintElem = target.nextElementSibling;
                    if (hintElem && hintElem.classList.contains("text-muted")) {
                        hintElem.classList.add("d-none");
                    }
                } else {
                    removeErrorField(target);
                    clearErrorMessage(target);
                    let hintElem = target.nextElementSibling;
                    if (hintElem && hintElem.classList.contains("text-muted")) {
                        hintElem.classList.remove("d-none");
                    }
                }
            } else {
                if (validation[target.name]) {
                    validation[target.name].validateFn(target);
                }
            }
        }
    }

    function validateAllFields(target) {
        Array.from(fields).forEach(function (field, index) {
            let currentIndexElem = Array.from(fields).findIndex(function (el) {
                return el.name === target.name;
            });
            if (target.name !== field.name && index <= currentIndexElem) {
                validateForm(field);
            }

            if (field.getAttribute("disabled") === "true") {
                removeErrorField(field);
                clearErrorMessage(field);
            }
        });
    }

    form.addEventListener(
        "blur",
        function (e) {
            let target = e.target;
            validateForm(target);
            validateAllFields(target);
        },
        true
    );

    form.addEventListener(
        "input",
        function (e) {
            let target = e.target;
            if (target.type === "radio" || target.type === "checkbox") {
                validateForm(target);
                validateAllFields(target);
            }
        },
        true
    );

    form.addEventListener(
        "change",
        function (e) {
            let target = e.target;
            if (target.type === "select-one") {
                validateForm(target);
                validateAllFields(target);
            }
        },
        true
    );

    checkPeselInput();
    changeVisibilityInputsLocation(countryInput.value);
    changeVisibilityJob(statusJobInput.value);

    countryInput.addEventListener("input", function (e) {
        changeVisibilityInputsLocation(e.target.value);
    });


    nationalityInput.addEventListener("change", function () {

        if (this.value === 'Polish') {
            peselInput.setAttribute("required", "true");
            noPeselInput.setAttribute("disabled", "true");
            peselInput.removeAttribute("disabled",);
            noPeselInput.checked = false;

            document.querySelector("[for='id_pesel']").classList.remove("disabled");
            document.querySelector("[for='id_no_pesel']").classList.add("disabled");
        } else {
            peselInput.removeAttribute("required");
            noPeselInput.removeAttribute("disabled",);
            document.querySelector("[for='id_no_pesel']").classList.remove("disabled");
        }
    });

    statusJobInput.addEventListener("change", function () {
        changeVisibilityJob(this.value);
        statusJobInfoInput.innerText = "";
        if (statusOptions.hasOwnProperty(this.value)) {

            statusJobInfoInput.removeAttribute("disabled",);
            document.querySelector("[for='id_status_info']").classList.remove("disabled");

            var option = document.createElement("option");
            option.text = "---";
            option.value = "";
            statusJobInfoInput.appendChild(option);

            statusOptions[this.value].forEach(
                (el) => {
                    var option = document.createElement("option");
                    option.text = el;
                    option.value = el;
                    statusJobInfoInput.appendChild(option);
                }
            )


        } else {
            statusJobInfoInput.setAttribute("disabled", "true");
            document.querySelector("[for='id_status_info']").classList.add("disabled");

        }
        validateAllFields(this);
    });

    peselInput.addEventListener("input", function () {
        checkPeselInput();
    });

    noPeselInput.addEventListener("change", function () {
        checkPeselInput();
    });

    submitBtn.addEventListener("click", function (e) {
        checkPeselInput();

        Array.from(fields).forEach(function (field) {
            validateForm(field);
            validateAllFields(field);
        });

        let validationList = Object.values(validation).map(function (field) {
            if (!field.isRequired) {
                field.isValid = true;
            }

            return field && field.isValid;
        });

        let isValidForm = validationList.every(function (el) {
            return el === true;
        });

        if (!isValidForm) {
            showAlertOnSubmit();
            e.preventDefault();
        } else {
            hideAlertOnSubmit();
        }
    });

    function changeLanguage() {
        let setLang = document.querySelector(".js-set-language");
        let submitSetLang = document.querySelector(".js-submit-set-language");
        let changeLangBtn = document.querySelectorAll(".js-change-language");
        let currentLanguageText = document.querySelector(".js-current-language");

        currentLanguageText.textContent = setLang.value.toUpperCase();

        Array.from(changeLangBtn).forEach(function (button) {
            button.addEventListener(
                "click",
                function () {
                    let opts = setLang.options;
                    let lang = button.getAttribute("data-lang");
                    for (let i = 0; i < opts.length; i++) {
                        if (opts[i].value === lang) {
                            let langIndex = opts[i].index;
                            setLang.selectedIndex = langIndex;
                        }
                    }
                    submitSetLang.submit();
                    currentLanguageText.textContent = lang.toUpperCase();
                },
                true
            );
        });
    }

    changeLanguage();
}

document.addEventListener("DOMContentLoaded", loadRegisterForm);
