<template>
    
    <div v-if="lecture !==null" class="detail">
        <h3>
            {{lecture.lec_title}}
        </h3>
        <table class="lecture">
            <tr>
                <td>
                    <span>Video number:</span>
                    {{lecture.idx}}
                </td>
                <td>
                    <span>Category:</span>
                    {{lecture.lec_category}}
                </td>
                <td>
                    <span>Video length:</span>
                    {{lecture.lec_length}}
                </td>
            </tr>
            <tr>
                <td colspan="3" class="lec-pic">
                    <iframe width="560" height="315"
                        v-bind:src="'https://www.youtube.com/embed/' + lecture.lec_code"
                        frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
                        allowfullscreen></iframe>
                </td>
            </tr>
        </table>
        <div class="commentCount">
            <span>
                Comment: {{commentList.length}}
            </span>
        </div>
        <table class="comments">

            <!-- Each element in commentList in data is used in each tr -->
            <tr v-for="(comment, cmtIdx) in commentList" :key="cmtIdx">
                <td>
                    {{comment.lc_name}}
                </td>
                <td>
                    {{comment.lc_comment}}
                </td>
            </tr>
            <tr>
                <td>
                    <!-- This input is linked with inputName in data -->
                    <input v-model="inputName" placeholder="Name"/>
                </td>
                <td>
                    <!-- This input is linked with inputComment in data -->
                    <input v-model="inputComment" placeholder="Write comment."
                        v-on:keyup.enter="submitComment"/>
                </td>
            </tr>
        </table>
    </div>
</template>

<script>
export default {
    name: 'lecture-detail',

    data: function() {
        return {
            idx: null,
            lecture: null,
            commentList: [],
            inputName: '',
            inputComment: '',
            submitting: false
        }
    },

    methods: {
        // getter for comments
        getComments: function () {
            let _this = this
            // get comments from the address
            _this.$axios.get(`http://localhost:8000/api/lec_comments/${this.idx}/`)
            .then((response) => {
                // empty the exisiting commentList
                _this.commentList.splice(0, _this.commentList.length)
                // fill it up with comments from the server
                _this.commentList = _this.commentList.concat(response.data)
            })
        },
        // send new comment to server
        submitComment: function () {
            let _this = this
            // Stop if sending new comment is ongoing already or if name or comment is empty
            if (_this.submitting
                || _this.inputName.trim().length === 0
                || _this.inputComment.trim().length === 0) return

            _this.submitting = true

            // Things to send to server
            let toSend = {
                lec_idx: _this.idx,
                lc_name: _this.inputName,
                lc_comment: _this.inputComment
            }

            // Send comment to server (the below address)
            _this.$axios.post(`http://localhost:8000/api/lec_comments/${this.idx}`,
                _this.$qs.stringify(toSend), {
                    headers: { 'Content-Type': 'application/x-www-form-urlencoded' }

                // If we get the response that the message is sent
                }).then((response) => {
                    // get new comments
                    _this.getComments()

                    // empty name and commeent fields
                    _this.inputName = ''
                    _this.inputComment = ''

                    // Pause "sending" status
                    _this.submitting = false
                }
            )
        }
    },

    mounted() {
        let _this = this
        _this.idx = _this.$route.params.idx

        // get lectures according to the idx
        _this.$axios.get(`http://localhost:8000/api/lectures/${this.idx}`)
        .then((response) => {
            _this.lecture = reponse.data
        })

        _this.getComments()
    }
}
</script>

<style lang="scss" scoped>
    @import '.../assets/scss/lecture.scss'
</style>
