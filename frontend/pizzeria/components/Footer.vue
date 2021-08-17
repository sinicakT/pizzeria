<template>
  <footer>
    <v-container class="footer-container" col="11">
      <v-row>
        <v-col class="footer-info font-weight-bold" cols="12" sm="3">
          <div class="info-box">
            <v-row v-for="item in footer_info" class="py-1">
              {{ item }}
            </v-row>
          </div>
        </v-col>
        <v-col class="contact_numbers px-6 py-12 py-sm-0" cols="12" sm="5">
          <v-row v-for="item in phone_numbers">
            <h2>{{ item }}</h2>
          </v-row>
        </v-col>
        <v-col class="open-time font-weight-bold" cols="12" sm="4">
          <v-row>Otváracia doba:</v-row>
          <v-row v-for="item in open_hours">
            <v-col col="4" class="pl-10">{{ item.name }} :</v-col>
            <v-col col="8">{{ item.value }}</v-col>
          </v-row>
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
      letter-spacing: 0.6rem;
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
