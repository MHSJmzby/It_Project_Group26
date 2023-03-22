import { createRouter, createWebHistory } from 'vue-router'
import UserCenter from "@/views/Userviews/UserCenter";
import HistoryOrder from "@/views/Userviews/HistoryOrder";
import Schedule from "@/views/Managerviews/Schedule";
import Movies from "@/views/Managerviews/Movies";
import Login from "@/views/Login";
import Register from "@/views/Register";
import Booking from "@/views/Userviews/Booking";
import Test from "@/views/Test";
import User from "@/Layout/User";
import Manager from "@/Layout/Manager";
import DataAnalysis from "@/views/Managerviews/DataAnalysis";

const routes = [
  {
    path: '/',
    name: 'login',
    component: Login
  },
  {
    path: '/register',
    name: 'register',
    component: Register
  },
  {
    path: '/user',
    name: 'user',
    component: User,
    redirect: '/booking',
    children: [
      {
        path: '/booking',
        name: 'booking',
        component: Booking
      },
      {
        path: '/usercenter',
        name: 'usercenter',
        component: UserCenter
      },
      {
        path: '/historyorder',
        name: 'historyorder',
        component: HistoryOrder
      },
    ],

  },
  {
    path: '/manager',
    name: 'manager',
    component: Manager,
    redirect: '/movies',
    children: [
      {
        path: '/schedule',
        name: 'schedule',
        component: Schedule
      },
      {
        path: '/movies',
        name: 'movies',
        component: Movies
      },
      {
        path: '/dataAnalysis',
        name: 'dataAnalysis',
        component: DataAnalysis
      },
    ]
  },
    {
    path: '/test',
    name: 'test',
    component: Test
  },


]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
