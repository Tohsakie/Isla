<template>
    <div>
      <stripe-checkout
        ref="checkoutRef"
        mode="payment"
        :pk="publishableKey"
        :line-items="lineItems"
        :success-url="successURL"
        :cancel-url="cancelURL"
        @loading="v => loading = v"
      />
      <button @click="submit">Pay now!</button>
    </div>
  </template>
  
  <script>
  import { StripeCheckout } from '@vue-stripe/vue-stripe';
  export default {
    components: {
      StripeCheckout,
    },
    data () {
      this.publishableKey = "pk_test_51OmunqC7YewuLxN6sciokY0BtdO8XcTTFN2CgK8qSDZGZcgEmWh36npZKsn0MTvBFxyqqSz73GkfNqC6TZfKGM7X00yD5eFxDm";
      return {
        loading: false,
        lineItems: [
          {
            price: 'price_1OmzcnC7YewuLxN6W4I1hFCx',
            quantity: 1,
          },
        ],
        successURL: 'https://www.google.fr/',
        cancelURL: 'https://www.x.com/',
      };
    },
    methods: {
      submit () {
        this.$refs.checkoutRef.redirectToCheckout();
      },
    },
  };
  </script>