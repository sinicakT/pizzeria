<template>
  <footer>
    <v-container class="footer-container" col="11">
      <v-row>
        <v-col class="open-time text-lg-body-1 text-md-body-2 text-sm-subtitle-1 text-xs-body-2 font-weight-bold mx-md-auto pl-16 pt-6" cols="12" lg="4" md="4" sm="6">
          <v-row>Otváracia doba:</v-row>
          <v-row v-for="item in open_hours">
            <v-col lg="5" col="6" class="pl-10">{{ item.name }} :</v-col>
            <v-col lg="7" col="6">{{ item.value }}</v-col>
          </v-row>
        </v-col>
        <v-col class="contact_numbers px-6 py-12 py-sm-0 text-md-h6 text-md-subtitle-2 text-lg-h6" cols="12" lg="5" md="4" sm="6">
          <v-row v-for="item in phone_numbers">
            <h2>{{ item }}</h2>
          </v-row>
        </v-col>
        <v-col class="footer-info font-weight-bold" cols="12" lg="3" md="4">
          <div class="info-box">
            <v-row v-for="(item, index) in footer_info" class="py-1" :key="'info_box_' + i">
              {{ item }}
            </v-row>
          </div>
        </v-col>
      </v-row>
    </v-container>
  </footer>
</template>

<script>
import {FOOTER_INFO, OPEN_HOURS, PHONE_NUMBERS} from "assets/data/data";

export default {
  name: "Footer",
  data() {
    return {
      open_hours: OPEN_HOURS,
      phone_numbers: PHONE_NUMBERS,
      footer_info: FOOTER_INFO
    }
  },
}
</script>

<style scoped lang="scss">
footer {
  margin-top: 20px;
  width: 100%;
  overflow: hidden;

  background: rgba(15, 15, 15, 0.7);
  opacity: 0.8;
  padding: 10px;

  .footer-container {
    display: flex;
    align-content: center;
    justify-items: center;

    .footer-info {
      display: flex;
      align-items: center;
      justify-content: center;

      .info-box {
        display: flex;
        flex-direction: column;
        align-content: center;
        justify-items: center;
        letter-spacing: 4px;
      }
    }

    .open-time {
      padding-bottom: 20px;

      .col {
        padding-top: 0;
        padding-bottom: 0;
      }
    }

    .contact_numbers {
      @media(min-width: 960px) {
        letter-spacing: 0.3rem !important;
      }
      @media(min-width: 1264px) {
        letter-spacing: 0.6rem !important;
      }
      display: flex;
      flex-direction: column;
      justify-content: center;
      align-items: center;

      .row {
        display: flex;
        align-items: center;
      }
    }
  }
}
</style>
