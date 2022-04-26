# LHC Booking System

# Features
- Get a list of all the bookings
- *Delete* an existing booking
- Get a list of all the bookings based on a *Venue*
- Get a list of all the bookings based on a *Date*

# Packages used
## Django
Install using `pip install django`
## Django REST framework
Install using `pip install djangorestframework`

# API Endpoints
## List of all Bookings
### URL
`GET` - `bookings/`

## Book an Event
### URL
`POST` - `book/`
### Request JSON
<table>
  <tbody>
    <tr>
      <td>Name</td>
      <td>Description</td>
      <td>Example</td>
    </tr>
    <tr>
      <td>event</td>
      <td>Name of the event</td>
      <td>Lecture</td>
    </tr>
    <tr>
      <td>venue</td>
      <td>Name of the venue</td>
      <td>LA-101</td>
    </tr>
    <tr>
      <td>date</td>
      <td>Date of the event</td>
      <td>2022-04-26</td>
    </tr>
    <tr>
      <td>start_time</td>
      <td>Starting Time for the event</td>
      <td>11:30:00</td>
    </tr>
    <tr>
      <td>end_time</td>
      <td>Ending Time for the event</td>
      <td>12:30:00</td>
    </tr>
  </tbody>
</table>

## Delete an Existing Booking
### URL
`DELETE` - `deletebooking/<int:id>/`
### Parameters
<table>
    <tbody>
        <tr>
            <td>Name</td>
            <td>Description</td>
            <td>Example</td>
        </tr>
        <tr>
            <td>id</td>
            <td>The id of the booking</td>
            <td>1</td>
        </tr>
    </tbody>
</table>

## List of all Bookings for a Particular Venue
### URL
`GET` - `venue/<str:venue>/`
### Parameters
<table>
    <tbody>
        <tr>
            <td>Name</td>
            <td>Description</td>
            <td>Example</td>
        </tr>
        <tr>
            <td>venue</td>
            <td>The name of the venue</td>
            <td>LA-101</td>
        </tr>
    </tbody>
</table>

## List of all Bookings for a Particular Date
### URL
`GET` - `day/<int:year>/<int:month>/<int:day>/`
### Parameters
<table>
    <tbody>
        <tr>
            <td>Name</td>
            <td>Description</td>
            <td>Example</td>
        </tr>
        <tr>
            <td>year</td>
            <td>Year</td>
            <td>2022</td>
        </tr>
        <tr>
            <td>month</td>
            <td>Month</td>
            <td>4</td>
        </tr>
        <tr>
            <td>day</td>
            <td>Day</td>
            <td>26</td>
        </tr>
    </tbody>
</table>

