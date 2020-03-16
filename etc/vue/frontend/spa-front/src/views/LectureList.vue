<template>
    <div class="list">
        <!-- value of pageTitle in the data -->
        <h2>{{pageTitle}}</h2>
        <table class="lectures">
            <tr v-for="(lecture, lecIdx) in lectureList" :key="lecIdx" @click="toDetail(lecture.idx)">
                <td class="thumbnail">
                    <img v-bind:src="lecture.lec_thumb"/>
                </td>
                <td class="title">
                    <span>
                        {{lecture.lec_date}}
                    </span>
                    <br>
                    {{lecture.lec_title}}
                </td>
            </tr>
        </table>
    </div>
</template>

<script>
export default {
    name: 'lecture-list',

    // data from server
    data: funcion() {
        return {
            pageTitle: "list of videos",
            // As page made by Vue is opened, "mounted" function is executed, and it fill up lectureList.
            lectureList: [] 
        }
    },

    // define functions
    method: {
        toDetail: function (idx) {
            this.$router.push(`detail/${idx}`)
        }
    },

    // command executed as pages open
    mounted() {
        let _this = this

        // get data from the following address
        _this.$axios.get('http://localhost:8000/api/lectures')
        .then((response) => {
            response.data.map((item) => {
                _this.lectureList.push(item)
            })
        })
    }
}
</script>

<style lan="scss" scoped>
    @import '../assets/scss/lecture.scss'
</style>