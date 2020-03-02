// ver1: call back Hell
findMathTeacherGo3("12345")

function findMathTeacherGo3 (studentId) {
    searchStudentInfo(studentId,
        function (studentInfo) {
            let studentPersonalId = studentInfo["personalId"];
            let highSchoolName = studentInfo["highSchoolName"];
            searchHighSchoolDBAddress(highSchoolName,
                function (highSchoolDBAddress) {
                    searchLectureInHighSchool(highSchoolDBAddress, studentPersonalId,
                        function (listOfLectures) {
                            let lectureIdGo3Student = listOfLectures["Go3Math"];
                            searchLectureInfo(lectureIdGo3Student,
                                function (lectureInfo) {
                                    console.log(`Teacher: ${lectureInfo["teacherName"]}`);
                                }
                            )
                        }
                    )
                }
            )
        }
    )
}


function searchStudentInfo(studentId, toDoWithStudentInfo) {
    ajax(
        baseUrl = "student-info/" + studentId,
        function (response) {
            toDoWithStudentInfo(response);
        }
    );
}

function searchHighSchoolDBAddress(highSchoolName, toDoWithAddress) {
    ajax(
        baseUrl = "highschool-db/" + highSchoolName,
        function (response) {
            toDoWithAddress(response);
        }
    );
}

function searchLectureInHighSchool(highSchoolDBAddress, studentPersonalId, toDoWithLectureInfo) {
    ajax(
        baseUrl = "classes/" + highSchoolDBAddress + "/" + studentPersonalId,
        function (response) {
            toDoWithLectureInfo(response);
        }
    );
}

function searchLectureInfo(lectureIdOfStudent, toDoWithLectureId) {
    ajax(
        baseUrl = "class-info/" + lectureIdOfStudent,
        function(response) {
            toDoWithLectureId(response);
        }
    );
}
