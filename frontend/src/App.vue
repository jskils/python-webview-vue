<template>
  <v-layout class="rounded rounded-md">
    <v-app-bar title="Application bar">
      <RouterLink to="/">Go to Home</RouterLink>
      <RouterLink to="/test">Go to About</RouterLink>
    </v-app-bar>
    <v-main class="d-flex align-center justify-center" style="min-height: 300px;">
      <RouterView/>
    </v-main>
  </v-layout>
</template>
