// ver3: async/await
searchGo3MathTeacher("12345");

async function searchGo3MathTeacher (studentId) {
    let studentInfo = await searchStudentInfo(studentId);

    let studentPersonalId = studentInfo["personalId"];
    let highSchoolName = studentInfo["highSchoolName"];
    let highSchoolDBAddress = await searchHighSchoolDBAddress(studentPersonalId, highSchoolName);

    let lectureIdOfStudent = await searchLectureInHighSchool(highSchoolDBAddress, studentPersonalId);

    let lectureInfo = await searchLectureInfo(lectureIdOfStudent);
    
    console.log(`Teacher: ${lectureInfo["teacherName"]}`);
}



function searchStudentInfo(studentId) {
    return new Promise(function (resolve, reject) {
        ajax(baseUrl + "student-info/" + studentId,     // 1st arg: async task
        function (response) {                           // 2nd arg: callback function as getting the result from async task as input arg
            resolve(response);
        });
    });
}

// Here, it does not matter if you follow ver1 or ver2.
function searchHighSchoolDBAddress(studentPersonalId, highSchoolName) {
    return new Promise(function (resolve, reject) {
        ajax(baseUrl + "highschool-db/" + highSchoolName,
        function (response) {
            resolve(studentPersonalId, response);
        });
    });
}

function searchLectureInHighSchool(highSchoolDBAddress, studentPersonalId) {
    return new Promise(function (resolve, reject) {
        ajax(baseUrl + "classes/" + highSchoolDBAddress + "/" + studentPersonalId,
        function (response) {
            resolve(response);
        });
    });
}

function searchLectureInfo(lectureIdOfStudent) {
    return new Promise(function (resolve, reject) {
        ajax(baseUrl + "class-info/" + lectureIdOfStudent,
        function (response) {
            resolve(response);
        });
    });
}