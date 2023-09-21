import java.util.PriorityQueue;

public class ToyShop {
    //объявляю приватные поля массивов id, имя и частота выпадения
    private String[] id;
    private String[] name;
    private int[] frequency;
// создаю конструктор, который принимает три строки информации об игрушках.
//разбиваю на подстроки, запятая - разделитель
    public ToyShop(String info1, String info2, String info3) {
        String[] tigr = info1.split(",");
        String[] leon = info2.split(",");
        String[] jaguar = info3.split(",");
//создаю новые массивы и заполняю их значениями из разобранных строк
        id = new String[]{tigr[0], leon[0], jaguar[0]};
        name = new String[]{tigr[1], leon[1], jaguar[1]};
        frequency = new int[]{Integer.parseInt(tigr[2]), Integer.parseInt(leon[2]), Integer.parseInt(jaguar[2])};
    }
//метод добавления игрушек в коллекцию.
//Toy - это вложенный класс, который будет представлять игрушку.
    public void addingToyQueue() {
        PriorityQueue<Toy> toyPriorityQueue = new PriorityQueue<>();
//создаю новый объект Toy и добавляю его в PriorityQueue
        for (int i = 0; i < id.length; i++) {
            Toy toy = new Toy(id[i], name[i], frequency[i]);
            toyPriorityQueue.add(toy);
        }

        // Пример использования PriorityQueue:
        //в каждой итерации извлекаю игрушку с наибольшей частотой выпадения пока 
        //коллекция не останется пустой
        while (!toyPriorityQueue.isEmpty()) {
            Toy toy = toyPriorityQueue.poll();
            System.out.println(toy);
        }
    }
//класс Toy представляет игрушку
    private static class Toy implements Comparable<Toy> {
        private String id;
        private String name;
        private int frequency;

        public Toy(String id, String name, int frequency) {
            this.id = id;
            this.name = name;
            this.frequency = frequency;
        }
//сравниваю игрушки по частоте выпадения
        @Override
        public int compareTo(Toy otherToy) {
            return Integer.compare(this.frequency, otherToy.frequency);
        }
//переопределяем метод toString() для удобства вывода
        @Override
        public String toString() {
            return "Toy{" +
                    "id='" + id + '\'' +
                    ", name='" + name + '\'' +
                    ", frequency=" + frequency +
                    '}';
        }
    }

    public static void main(String[] args) {
        String info1 = "1,tigr,5";
        String info2 = "2,leon,3";
        String info3 = "3,jaguar,7";

        ToyShop toyCollection = new ToyShop(info1, info2, info3);
        toyCollection.addingToyQueue();
    }
}