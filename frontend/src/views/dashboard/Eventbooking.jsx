import React, { useState, useEffect } from "react";
import axios from "axios";
import Header from "../partials/Header";
import Footer from "../partials/Footer";

function Eventbooking() {
    const [events, setEvents] = useState([]);
    const [view, setView] = useState("list");
    const [newEvent, setNewEvent] = useState({
        name: "",
        date: "",
        time: "",
        location: "",
        description: "",
    });

    // Fetch events from the backend
    useEffect(() => {
        axios.get("http://127.0.0.1:8000/api/events/")
            .then(response => setEvents(response.data))
            .catch(error => console.error("Error fetching events:", error));
    }, []);

    // Handle form input changes
    const handleInputChange = (e) => {
        const { name, value } = e.target;
        setNewEvent({ ...newEvent, [name]: value });
    };

    // Handle form submission
    const handleCreateEvent = (e) => {
        e.preventDefault();
        axios.post("http://127.0.0.1:8000/api/events/", newEvent)
            .then(response => {
                setEvents([...events, response.data]);
                setNewEvent({ name: "", date: "", time: "", location: "", description: "" });
                setView("list");
            })
            .catch(error => console.error("Error creating event:", error));
    };

    // Render the appropriate view
    const renderView = () => {
        switch (view) {
            case "list":
                return (
                    <section className="pb-8 mt-5">
                        <div className="card">
                            <div className="card-header border-bottom px-4 py-3">
                                <h4 className="mb-0">Event List</h4>
                            </div>
                            <div className="card-body">
                                {events.map(event => (
                                    <div key={event.id} className="mb-3">
                                        <h5>{event.name}</h5>
                                        <p>Date: {event.date}</p>
                                        <p>Location: {event.location}</p>
                                        <button
                                            className="btn btn-primary"
                                            onClick={() => setView("details")}
                                        >
                                            View Details
                                        </button>
                                    </div>
                                ))}
                                <button
                                    className="btn btn-success"
                                    onClick={() => setView("create")}
                                >
                                    Create Event
                                </button>
                            </div>
                        </div>
                    </section>
                );
            case "create":
                return (
                    <section className="pb-8 mt-5">
                        <div className="card mb-3">
                            <div className="card-header border-bottom px-4 py-3">
                                <h4 className="mb-0">Create Event</h4>
                            </div>
                            <div className="card-body">
                                <form onSubmit={handleCreateEvent}>
                                    <div className="mb-3">
                                        <label className="form-label">Event Name</label>
                                        <input
                                            className="form-control"
                                            type="text"
                                            name="name"
                                            value={newEvent.name}
                                            onChange={handleInputChange}
                                            required
                                        />
                                    </div>
                                    <div className="mb-3">
                                        <label className="form-label">Event Date</label>
                                        <input
                                            className="form-control"
                                            type="date"
                                            name="date"
                                            value={newEvent.date}
                                            onChange={handleInputChange}
                                            required
                                        />
                                    </div>
                                    <div className="mb-3">
                                        <label className="form-label">Event Time</label>
                                        <input
                                            className="form-control"
                                            type="time"
                                            name="time"
                                            value={newEvent.time}
                                            onChange={handleInputChange}
                                            required
                                        />
                                    </div>
                                    <div className="mb-3">
                                        <label className="form-label">Event Location</label>
                                        <input
                                            className="form-control"
                                            type="text"
                                            name="location"
                                            value={newEvent.location}
                                            onChange={handleInputChange}
                                            required
                                        />
                                    </div>
                                    <div className="mb-3">
                                        <label className="form-label">Event Description</label>
                                        <textarea
                                            className="form-control"
                                            rows="5"
                                            name="description"
                                            value={newEvent.description}
                                            onChange={handleInputChange}
                                            required
                                        ></textarea>
                                    </div>
                                    <button type="submit" className="btn btn-success">
                                        Create Event
                                    </button>
                                </form>
                            </div>
                        </div>
                    </section>
                );
            default:
                return null;
        }
    };

    return (
        <>
            <Header />
            <section className="pt-5 pb-5">
                <div className="container">
                    <div className="row mt-0 mt-md-4">
                        <div className="col-lg-12 col-md-8 col-12">
                            <section className="py-4 py-lg-6 bg-primary rounded-3">
                                <div className="container">
                                    <div className="row">
                                        <div className="offset-lg-1 col-lg-10 col-md-12 col-12">
                                            <div className="d-lg-flex align-items-center justify-content-between">
                                                <div className="mb-4 mb-lg-0">
                                                    <h1 className="text-white mb-1">
                                                        {view === "list" && "Upcoming Events"}
                                                        {view === "create" && "Create Event"}
                                                    </h1>
                                                </div>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </section>
                            {renderView()}
                        </div>
                    </div>
                </div>
            </section>
            <Footer />
        </>
    );
}

export default Eventbooking;