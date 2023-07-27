const app = new Vue({
    el: '#app',
    data: {
        workout: '',
        workouts: [],
        goal: null,
        goalSet: false,
        chartData: null
    },
    methods: {
        addWorkout() {
            if (this.workout.trim() !== '') {
                this.workouts.push(this.workout);
                this.workout = '';
            }
        },
        setGoal() {
            if (this.goal !== null) {
                this.goalSet = true;
            }
        },
        generateChartData() {
            // Replace this with your data to generate charts and graphs
            this.chartData = {
                labels: ['Day 1', 'Day 2', 'Day 3', 'Day 4', 'Day 5'],
                datasets: [
                    {
                        label: 'Workout Duration',
                        backgroundColor: 'rgba(75, 192, 192, 0.2)',
                        borderColor: 'rgba(75, 192, 192, 1)',
                        borderWidth: 1,
                        data: [30, 45, 50, 40, 60]
                    }
                ]
            };

            this.renderChart();
        },
        renderChart() {
            const ctx = this.$refs.chart.getContext('2d');
            const myChart = new Chart(ctx, {
                type: 'bar',
                data: this.chartData,
                options: {
                    responsive: true,
                    maintainAspectRatio: false
                }
            });
        }
    },
    mounted() {
        this.generateChartData();
    }
});

