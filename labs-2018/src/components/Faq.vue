<template>
  <div>
    <h1>Frequently Asked Questions</h1>
    <p>We know you lovelies have questions, and we have some of the answers! We've collected some of our most common questions and answered them all here.</p>
    
        <faqCard 
          v-for="faq in faqs.questions" 
          :question="faq.question"
          :answer="faq.answer"
          :note="faq.note"
          :key="faq.id"
        />
  </div>
</template>

<script>
import { mapState } from "vuex"
import  faqCard  from "./FaqCard"

export default {
  computed: mapState({
    faqs: state => state.faqs
  }),

  components:{
    faqCard
  }
}
</script>
