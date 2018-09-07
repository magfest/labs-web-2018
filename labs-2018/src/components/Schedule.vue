<template>
<v-container>
  <h1>MAGLabs 2018 Schedule</h1>
  <v-card>
    <br/>
    <h3>Printed Schedule</h3>
    <iframe src="https://drive.google.com/file/d/1zoNpRv1AIwieU1OGm_9l5ciopd_y_xPz/preview" width="800" height="600"></iframe>
    <br/>
  </v-card>
  <br>
  <h3>Panels Schedule</h3>
  <iframe src="https://calendar.google.com/calendar/b/1/embed?title=Panels%20Schedule&amp;mode=WEEK&amp;height=600&amp;wkst=2&amp;bgcolor=%23FFFFFF&amp;src=magfest.org_90q7g43cq89sks37s2aclsceg0%40group.calendar.google.com&amp;color=%235229A3&amp;src=magfest.org_n37mp8h5d9c3ugf1shkne3ubo0%40group.calendar.google.com&amp;color=%23691426&amp;src=magfest.org_fqkt35fbj7g8c01rp8n1io67oo%40group.calendar.google.com&amp;color=%23865A5A&amp;ctz=America%2FNew_York"
    style="border-width:0" width="800" height="600" frameborder="0" scrolling="no"></iframe>
</v-container>
</template>

<script>
import {
  mapState
} from "vuex"

export default {
  computed: mapState({}),

}
</script>
