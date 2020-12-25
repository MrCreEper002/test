cities = ['Абаза', 'Абакан', 'Абвиль', 'Абдулино', 'Абиджан', 'Абинск', 'Абу-Даби', 'Абуджа', 'Авиньон', 'Агидель',
          'Агадир', 'Агрыз', 'Адана', 'Аддис-Абеба', 'Аделаида', 'Адыгейск', 'Азнакаево', 'Азов', 'Ак-Довурак',
          'Акка', 'Аккра', 'Аксай', 'Актау', 'Актюбинск', 'Алагир', 'Алапаевск', 'Алатырь', 'Алдан',
          'Алейск', 'Александрия', 'Алжир', 'Александров', 'Александровск', 'Александровск-Сахалинский',
          'Алексеевка', 'Алексин', 'Алжир', 'Алзамай', 'Алма-Ата', 'Альметьевск', 'Амман', 'Амстердам',
          'Амурск', 'Амьен', 'Анадырь', 'Анапа', 'Ангарск', 'Андреаполь', 'Анжеро-Судженск', 'Анива', 'Анкара',
          'Анталья', 'Антананариву', 'Антверпен', 'Аньшань', 'Апатиты', 'Апиа', 'Апрелевка', 'Апшеронск', 'Арамиль',
          'Аргун', 'Ардатов', 'Ардон', 'Арзамас', 'Аркадак', 'Арль', 'Армавир', 'Арнем', 'Арсеньев', 'Артём',
          'Артёмовск', 'Артёмовский', 'Архангельск', 'Асбест', 'Асино', 'Астана', 'Астрахань', 'Асунсьон',
          'Аткарск', 'Атырау', 'Афины', 'Ахмадабад', 'Ахтубинск', 'Ачинск', 'Аша', 'Ашдод', 'Ашкелон', 'Ашхабад',
          'Бабаево', 'Бабушкин', 'Бавлы', 'Багдад', 'Багратионовск', 'Базель', 'Байкальск', 'Баймак', 'Бакал',
          'Баксан', 'Баку', 'Балабаново', 'Балаково', 'Балахна', 'Балашиха', 'Балашов', 'Балей', 'Балтийск',
          'Балыкчи', 'Бангалор', 'Бангкок', 'Бандунг', 'Барабинск', 'Барнаул', 'Барранкилья', 'Барселона', 'Барыш',
          'Батайск', 'Баткен', 'Батуми', 'Бежецк', 'Бейрут', 'Белая Калитва', 'Белая Холуница', 'Белгород',
          'Белград', 'Белебей', 'Белёв', 'Белинский', 'Белово', 'Белогорск', 'Белозерск', 'Белокуриха', 'Беломорск',
          'Белорецк', 'Белореченск', 'Белоусово', 'Белоярский', 'Белу-Оризонти', 'Бельфор', 'Белый', 'Берген',
          'Бердск', 'Березники', 'Берёзовский', 'Берн', 'Берлин', 'Беслан', 'Бийск', 'Бикин', 'Билибино',
          'Биньямина', 'Бирмингем', 'Биробиджан', 'Бирск', 'Бирюсинск', 'Бирюч', 'Бишкек', 'Благовещенск',
          'Благодарный', 'Блед', 'Бобров', 'Бобруйск', 'Богданович', 'Богородицк', 'Богородск', 'Богота', 'Боготол',
          'Богучар', 'Бодайбо', 'Бокситогорск', 'Болгар', 'Бологое', 'Болотное', 'Болохово', 'Болхов',
          'Большой Камень', 'Бор', 'Бордо', 'Борзя', 'Борисов', 'Борисоглебск', 'Боровичи', 'Боровск', 'Бородино',
          'Бохум', 'Бразилиа', 'Братислава', 'Братск', 'Бреда', 'Бремен', 'Брест', 'Брисбен', 'Бристоль', 'Брно',
          'Бронницы', 'Брюгге', 'Брюссель', 'Брянск', 'Бугульма', 'Бугуруслан', 'Будапешт', 'Будённовск', 'Бузулук',
          'Буинск', 'Буй', 'Буйнакск', 'Бутурлиновка', 'Бухара', 'Бухарест', 'Буэнос-Айрес', 'Бхопал', 'Вадодара',
          'Валдай', 'Валенсия', 'Валуйки', 'Варна', 'Варшава', 'Вашингтон', 'Веймар', 'Велиж', 'Великие Луки',
          'Великий Новгород', 'Великий Устюг', 'Веллингтон', 'Вельск', 'Вена', 'Венеция', 'Венёв', 'Вентспислс',
          'Верещагино', 'Верея', 'Вернигнроде', 'Верхнеуральск', 'Верхний Тагил', 'Верхний Уфалей', 'Верхняя Пышма',
          'Верхняя Салда', 'Верхняя Тура', 'Верхотурье', 'Верхоянск', 'Весьегонск', 'Ветлуга', 'Видное', 'Вильнюс',
          'Вилюйск', 'Вилючинск', 'Витебск', 'Вихоревка', 'Вичуга', 'Владивосток', 'Владикавказ', 'Владимир',
          'Волгоград', 'Волгодонск', 'Волгореченск', 'Волжск', 'Волжский', 'Вологда', 'Володарск', 'Волоколамск',
          'Волосово', 'Волхов', 'Волчанск', 'Вольск', 'Воркута', 'Воронеж', 'Ворсма', 'Воскресенск', 'Воткинск',
          'Вроцлав', 'Всеволожск', 'Вуктыл', 'Выборг', 'Выкса', 'Высоковск', 'Высоцк', 'Вытегра', 'Вышний Волочёк',
          'Вяземский', 'Вязники', 'Вязьма', 'Вятские Поляны', 'Гаага', 'Гавана', 'Гаврилов Посад', 'Гаврилов-Ям',
          'Гагарин', 'Гагра', 'Гай', 'Галич', 'Галле', 'Гамбург', 'Ганновер', 'Гаосюн', 'Гатчина', 'Гауда',
          'Гвадалахара', 'Гвардейск', 'Гватемала', 'Гданьск', 'Гдов', 'Геленджик', 'Гент', 'Георгиевск', 'Гётеборг',
          'Гирин', 'Глазго', 'Глазов', 'Голицыно', 'Гонконг', 'Гомель', 'Горбатов', 'Горно-Алтайск', 'Горнозаводск',
          'Горняк', 'Городец', 'Городище', 'Городовиковск', 'Гороховец', 'Горячий Ключ', 'Грайворон', 'Гремячинск',
          'Гродно', 'Грозный', 'Гронинген', 'Грязи', 'Грязовец', 'Гуанчжоу', 'Гуаякиль', 'Губаха', 'Губкин',
          'Губкинский', 'Гудермес', 'Гуйян', 'Гуково', 'Гулькевичи', 'Гурьевск', 'Гусев', 'Гусиноозёрск',
          'Гусь-Хрустальный', 'Давлеканово', 'Дагестанские Огни', 'Дакар', 'Дакка', 'Даллас', 'Далматово',
          'Дальнегорск', 'Дальнереченск', 'Далянь', 'Дамаск', 'Данилов', 'Данков', 'Дар-эс-Салам', 'Даугавпилс',
          'Дегтярск', 'Дедовск', 'Делфт', 'Дели', 'Демидов', 'Дербент', 'Десногорск', 'Джайпур', 'Джакарта',
          'Дзержинск', 'Дзержинский', 'Дивногорск', 'Дигора', 'Димитровград', 'Дмитриев-Льговский', 'Дмитров',
          'Дмитровск', 'Днепр', 'Дно', 'Добрянка', 'Долгопрудный', 'Долинск', 'Домодедово',
          'Донецк', 'Донской', 'Дорогобуж', 'Дрезден', 'Дрезна', 'Дуала', 'Дубай', 'Дублин', 'Дубна', 'Дубовка',
          'Дубровник', 'Дудинка', 'Духовщина', 'Душанбе', 'Дюнкерк', 'Дюртюли', 'Дюссельдорф', 'Дятьково',
          'Евпатория', 'Егорьевск', 'Ейск', 'Екатеринбург', 'Елабуга', 'Елец', 'Елизово', 'Ельня', 'Еманжелинск',
          'Емва', 'Енисейск', 'Ереван', 'Ершов', 'Ессентуки', 'Ефремов', 'Железноводск', 'Железногорск',
          'Железногорск', 'Железногорск-Илимский', 'Железнодорожный', 'Женева', 'Жердевка', 'Жигулёвск', 'Жиздра',
          'Жирновск', 'Житомир', 'Жуков', 'Жуковка', 'Жуковский', 'Завитинск', 'Заводоуковск', 'Заволжск',
          'Заволжье', 'Загреб', 'Задонск', 'Заинск', 'Закаменск', 'Заозёрный', 'Заозёрск', 'Западная Двина',
          'Заполярный', 'Запорожье', 'Зарайск', 'Заречный', 'Заречный', 'Заринск', 'Звенигово', 'Звенигород',
          'Зверево', 'Зволле', 'Зеленогорск', 'Зеленогорск', 'Зеленоград', 'Зеленоградск', 'Зеленодольск',
          'Зеленокумск', 'Зерноград', 'Зея', 'Зима', 'Зихрон Яаков', 'Златоуст', 'Злынка', 'Змеиногорск',
          'Знаменск', 'Зубцов', 'Зуевка', 'Ибадан', 'Ивангород', 'Иваново', 'Ивано-Франковск', 'Ивантеевка',
          'Ивдель', 'Игарка', 'Иерусалим', 'Ижевск', 'Избербаш', 'Измир', 'Изобильный', 'Иланский', 'Индаур',
          'Инза', 'Инсар', 'Инсбрук', 'Инта', 'Инчхон', 'Иоккаити', 'Иокогама', 'Ипатово', 'Ирбит', 'Иркутск',
          'Исилькуль', 'Искитим', 'Искогама', 'Исламабад', 'Ист-Дерри', 'Истра', 'Исфахан', 'Ишим', 'Ишимбай',
          'Кавасаки', 'Кадис', 'Кадников', 'Казань', 'Каир', 'Кайеркан', 'Калач', 'Калач-на-Дону', 'Калачинск',
          'Кале', 'Кали', 'Калининград', 'Калининск', 'Калтан', 'Калуга', 'Калькутта', 'Кальян', 'Калязин',
          'Камакура', 'Камбарка', 'Каменка', 'Каменногорск', 'Каменск-Уральский', 'Каменск-Шахтинский',
          'Камень-на-Оби', 'Камешково', 'Камызяк', 'Камышин', 'Камышлов', 'Канаш', 'Кандалакша', 'Канны',
          'Канпур', 'Канск', 'Кант', 'Карабаново', 'Карабаш', 'Карабулак', 'Караганда', 'Каракас', 'Каракол',
          'Карасук', 'Карачаевск', 'Карачев', 'Карачи', 'Каргат', 'Каргополь', 'Каркассон', 'Карловы Вары',
          'Карлсруэ', 'Кармиэль', 'Карпинск', 'Картахена', 'Карталы', 'Касабланка', 'Касимов', 'Касли', 'Каспийск',
          'Катав-Ивановск', 'Катайск', 'Катакюсю', 'Каунас', 'Кацуяма', 'Качканар', 'Кашин', 'Кашира', 'Кванджу',
          'Кедровый', 'Кемерово', 'Кемь', 'Кесон-Сити', 'Кёльн', 'Кзыл-Орда', 'Киев', 'Кизел', 'Кизилюрт', 'Кизляр',
          'Киль', 'Кимовск', 'Кимры', 'Кингисепп', 'Кинель', 'Кинешма', 'Киншаса', 'Киреевск', 'Киркенес', 'Киото',
          'Киренск', 'Киржач', 'Кириллов', 'Кириши', 'Киров', 'Кировград', 'Кировоград', 'Кирово-Чепецк', 'Кировск',
          'Кировск', 'Кирс', 'Кирсанов', 'Кирьят-Шмона', 'Киселёвск', 'Кисловодск', 'Кито', 'Кишинев', 'Клайпеда',
          'Кливленд', 'Климовск', 'Клин', 'Клинцы', 'Княгинино', 'Кобе', 'Ковдор', 'Ковентри', 'Ковров',
          'Ковылкино', 'Когалым', 'Кодинск', 'Козельск', 'Козловка', 'Козьмодемьянск', 'Коканд', 'Кола', 'Кологрив',
          'Коломна', 'Колпашево', 'Колпино', 'Кольчугино', 'Коммунар', 'Компьень', 'Комсомольск',
          'Комсомольск-на-Амуре', 'Конаково', 'Конакри', 'Кондопога', 'Кондрово', 'Константиновск', 'Копейск',
          'Копенгаген', 'Кораблино', 'Кордова', 'Кореновск', 'Коркино', 'Королёв', 'Короча', 'Корсаков', 'Коряжма',
          'Костерёво', 'Костомукша', 'Кострома', 'Котельники', 'Котельниково', 'Котельнич', 'Котлас', 'Котово',
          'Котовск', 'Кохма', 'Краков', 'Красавино', 'Красноармейск', 'Красноармейск', 'Красновишерск',
          'Красногорск', 'Краснодар', 'Красное Село', 'Краснозаводск', 'Краснознаменск', 'Краснознаменск',
          'Краснокаменск', 'Краснокамск', 'Краснослободск', 'Краснослободск', 'Краснотурьинск', 'Красноуральск',
          'Красноуфимск', 'Красноярск', 'Красный Кут', 'Красный Сулин', 'Красный Холм', 'Кремёнки', 'Кронштадт',
          'Кропоткин', 'Крымск', 'Кстово', 'Куала-Лумпур', 'Кубинка', 'Кувандык', 'Кувшиново', 'Кудымкар',
          'Кузнецк', 'Кулебаки', 'Кумертау', 'Кунгур', 'Куньмин', 'Купино', 'Курган', 'Курганинск', 'Курильск',
          'Курлово', 'Куровское', 'Курск', 'Куртамыш', 'Курчатов', 'Куса', 'Кустанай', 'Кушва', 'Кызыл', 'Кыштым',
          'Кяхта', 'Ла-Пас', 'Лабинск', 'Лабытнанги', 'Лагань', 'Лагос', 'Лаишево', 'Лакинск', 'Лакхнау',
          'Лангепас', 'Ланьчжоу', 'Лаc-Вегас', 'Лахденпохья', 'Лахор', 'Лебедянь', 'Лейден', 'Лейпциг', 'Лелистад',
          'Ле-Ман', 'Лениногорск', 'Ленинск', 'Ленинск-Кузнецкий', 'Ленск', 'Лермонтов', 'Лесной', 'Лесозаводск',
          'Лесосибирск', 'Ливерпуль', 'Ливны', 'Лидс', 'Ликино-Дулёво', 'Лилль', 'Лима', 'Лимассол', 'Лимож',
          'Линкопинг', 'Линц', 'Лион', 'Липецк', 'Липки', 'Лиски', 'Лиссабон', 'Лихославль', 'Лобня',
          'Лодейное Поле', 'Лозанна', 'Ломоносов', 'Лондон', 'Лос-Анджелес', 'Лосино-Петровский', 'Луанда', 'Лувен',
          'Луга', 'Луганск', 'Лудхияна', 'Луза', 'Лукоянов', 'Луховицы', 'Луцк', 'Лысково', 'Лысьва', 'Лыткарино',
          'Львов', 'Любань', 'Люберцы', 'Любим', 'Люксембург', 'Люцерн', 'Лянтор', 'Мааслуис', 'Маастрихт',
          'Магадан', 'Магас', 'Магдебург', 'Магнитогорск', 'Мадрас', 'Мадрид', 'Майкоп', 'Майский', 'Майами-Бич',
          'Макарьев', 'Макушино', 'Малага', 'Малая Вишера', 'Малгобек', 'Малмыж', 'Малоархангельск',
          'Малоярославец', 'Мамадыш', 'Мамоново', 'Манаус', 'Манила', 'Мантурово', 'Манчестер', 'Мапуту',
          'Маракайбо', 'Мариинск', 'Мариинский Посад', 'Маркс', 'Марракеш', 'Марсель', 'Маршалл', 'Махачкала',
          'Мглин', 'Мегион', 'Медан', 'Медвежьегорск', 'Медельин', 'Медногорск', 'Медынь', 'Межгорье',
          'Междуреченск', 'Мезень', 'Меленки', 'Мелеуз', 'Мельбурн', 'Менделеевск', 'Мензелинск', 'Мехико',
          'Мешхед', 'Мещовск', 'Миасс', 'Мидделбург', 'Микунь', 'Милан', 'Миллерово', 'Минеральные Воды', 'Минск',
          'Минусинск', 'Миньяр', 'Мирный', 'Мирный', 'Михайлов', 'Михайловка', 'Михайловск', 'Михайловск',
          'Мичуринск', 'Могилёв', 'Могоча', 'Можайск', 'Можга', 'Моздок', 'Монреаль', 'Монтевидео', 'Монтеррей',
          'Монтре', 'Мончегорск', 'Морозовск', 'Моршанск', 'Мосальск', 'Москва', 'Московский', 'Мосс', 'Мостар',
          'Мумбаи', 'Муравленко', 'Мураши', 'Мурманск', 'Муром', 'Мценск', 'Мыски', 'Мытищи', 'Мышкин', 'Мюнхен',
          'Набережные Челны', 'Навашино', 'Наволоки', 'Нагоя', 'Нагпур', 'Надым', 'Назарет', 'Назарово', 'Назрань',
          'Называевск', 'Найменген', 'Найроби', 'Нальчик', 'Нанкин', 'Наньчан', 'Нарва', 'Нариманов',
          'Наро-Фоминск', 'Нарткала', 'Нарьян-Мар', 'Нарын', 'Нахичевань', 'Находка', 'Неаполь', 'Невель',
          'Невельск', 'Невинномысск', 'Невьянск', 'Нелидово', 'Неман', 'Нерехта', 'Нерчинск', 'Нерюнгри',
          'Несаулькойотль', 'Несвиж', 'Нестеров', 'Нефтегорск', 'Нефтекамск', 'Нефтекумск', 'Нефтеюганск', 'Нея',
          'Нижневартовск', 'Нижнекамск', 'Нижнеудинск', 'Нижние Серги', 'Нижний Ломов', 'Нижний Новгород',
          'Нижний Тагил', 'Нижняя Салда', 'Нижняя Тура', 'Николаев', 'Николаевск', 'Николаевск-на-Амуре',
          'Никольск', 'Никольск', 'Никольское', 'Никосия', 'Ницца', 'Новая Ладога', 'Новая Ляля',
          'Новоалександровск', 'Новоалтайск', 'Новоаннинский', 'Нововоронеж', 'Новодвинск', 'Новозыбков',
          'Новокубанск', 'Новокузнецк', 'Новокуйбышевск', 'Новомичуринск', 'Новомосковск', 'Новопавловск',
          'Новоржев', 'Новороссийск', 'Новосибирск', 'Новосиль', 'Новосокольники', 'Новотроицк', 'Новоузенск',
          'Новоульяновск', 'Новоуральск', 'Новохопёрск', 'Новочебоксарск', 'Новочеркасск', 'Новошахтинск',
          'Новый Оскол', 'Новый Уренгой', 'Ногинск', 'Нолинск', 'Норильск', 'Ноябрьск', 'Нукуалофа', 'Нурлат',
          'Нью-Дели', 'Нью-Йорк', 'Нытва', 'Нюрба', 'Нягань', 'Нязепетровск', 'Няндома', 'Облучье', 'Обнинск',
          'Обоянь', 'Обь', 'Одесса', 'Одинцово', 'Ожерелье', 'Озёрск', 'Озёрск', 'Озёры', 'Окленд', 'Октябрьск',
          'Октябрьский', 'Окуловка', 'Олёкминск', 'Оленегорск', 'Оломоуц', 'Олонец', 'Ольштын', 'Омдурман', 'Омск',
          'Омута', 'Омутнинск', 'Онега', 'Опочка', 'Орёл', 'Оренбург', 'Орехово-Зуево', 'Орлов', 'Орск', 'Орхус',
          'Оса', 'Осака', 'Осинники', 'Осло', 'Осташков', 'Остров', 'Островной', 'Острогожск', 'Отрадное',
          'Отрадный', 'Оттава', 'Оха', 'Оханск', 'Очёр', 'Ош', 'Павлово', 'Павловск', 'Павловск',
          'Павловский Посад', 'Павлодар', 'Палембанг', 'Палермо', 'Палласовка', 'Пангаи', 'Паневежис', 'Париж',
          'Партизанск', 'Певек', 'Пенза', 'Первомайск', 'Первоуральск', 'Перевоз', 'Пересвет',
          'Переславль-Залесский', 'Пекин', 'Пермь', 'Перт', 'Пестово', 'Петах-Тиква', 'Петергоф/ Петродворец',
          'Петров Вал', 'Петровск', 'Петровск-Забайкальский', 'Петрозаводск', 'Петропавловск-Камчатский',
          'Петухово', 'Петушки', 'Печора', 'Печоры', 'Пикалёво', 'Пионерский', 'Питкяранта', 'Плёс', 'Плавск',
          'Пласт', 'Поворино', 'Подольск', 'Подпорожье', 'Познань', 'Покачи', 'Покров', 'Покровск', 'Полевской',
          'Полесск', 'Полоцк', 'Полтава', 'Полысаево', 'Полярные Зори', 'Полярный', 'Поронайск', 'Портленд',
          'Порту-Алегри', 'Порхов', 'Потсдам', 'Похвистнево', 'Почеп', 'Починок', 'Пошехонье', 'Правдинск', 'Прага',
          'Приволжск', 'Приморск', 'Приморск', 'Приморско-Ахтарск', 'Приозерск', 'Провиденс', 'Прокопьевск',
          'Пролетарск', 'Протвино', 'Прохладный', 'Псков', 'Пугачёв', 'Пудож', 'Пуна', 'Пусан', 'Пустошка', 'Пучеж',
          'Пушкин', 'Пушкино', 'Пущино', 'Пуэбла', 'Пхеньян', 'Пыталово', 'Пыть-Ях', 'Пятигорск', 'Рабат',
          'Радужный', 'Радужный', 'Райчихинск', 'Раменское', 'Рассказово', 'Ревда', 'Реж', 'Резекне', 'Реймс',
          'Ресифи', 'Реутов', 'Ржев', 'Рига', 'Рим', 'Рио-де-Жанейро', 'Ричмонд', 'Ришон-ле-Цион', 'Ровно',
          'Родники', 'Рославль', 'Россошь', 'Ростов', 'Ростов-на-Дону', 'Росток', 'Роттердам', 'Рошаль', 'Ртищево',
          'Рубцовск', 'Рудня', 'Руза', 'Рузаевка', 'Рыбинск', 'Рыбное', 'Рыльск', 'Ряжск', 'Рязань', 'Салават',
          'Салаир', 'Салвадор', 'Салехард', 'Салинас', 'Сало', 'Сальск', 'Самара', 'Самарканд', 'Сан-Антонио',
          'Сан-Диего', 'Санкт-Петербург', 'Сан-Паулу', 'Санто-Доминго', 'Сантьяго', 'Сан-Франциско', 'Сан-Хосе',
          'Сан-Хусто', 'Саппоро', 'Саранск', 'Сарапул', 'Саратов', 'Саров', 'Сасово', 'Сатка', 'Сафоново',
          'Саяногорск', 'Саянск', 'Светлогорск', 'Светлоград', 'Светлый', 'Светогорск', 'Свирск', 'Свободный',
          'Себеж', 'Севастополь', 'Северо-Курильск', 'Северобайкальск', 'Северодвинск', 'Североморск',
          'Североуральск', 'Северск', 'Севск', 'Сегежа', 'Сельцо', 'Семаранг', 'Семёнов', 'Семикаракорск',
          'Семилуки', 'Семипалатинск', 'Сенгилей', 'Сент-пол', 'Серафимович', 'Сергач', 'Сергиев Посад', 'Сердобск',
          'Серов', 'Серпухов', 'Сертолово', 'Сестрорецк', 'Сеул', 'Сиань', 'Сибай', 'Сидней', 'Силламяэ', 'Сим',
          'Симферополь', 'Сингапур', 'Сковородино', 'Скопин', 'Славгород', 'Славск', 'Славянск-на-Кубани', 'Сланцы',
          'Слободской', 'Слюдянка', 'Смоленск', 'Снежинск', 'Снежногорск', 'Собинка', 'Советск', 'Советск',
          'Советск', 'Советская Гавань', 'Советский', 'Сокол', 'Сокольники', 'Солигалич', 'Соликамск',
          'Солнечногорск', 'Соль-Илецк', 'Сольвычегодск', 'Солт-Лейк-Сити', 'Сольцы', 'Сорочинск', 'Сорск',
          'Сортавала', 'Сосенский', 'Сосновка', 'Сосновоборск', 'Сосногорск', 'София', 'Сочи',
          'Спас-Деменск', 'Спас-Клепики', 'Спасск', 'Спасск-Дальний', 'Спасск-Рязанский', 'Сплит', 'Спрингфилд',
          'Среднеколымск', 'Среднеуральск', 'Сретенск', 'Ставрополь', 'Стамбул', 'Старая Купавна', 'Старая Русса',
          'Старица', 'Стародуб', 'Старый Оскол', 'Степанакерт', 'Стерлитамак', 'Стокгольм', 'Страсбург',
          'Стрежевой', 'Строитель', 'Струнино', 'Ступино', 'Суворов', 'Суджа', 'Судогда', 'Суздаль', 'Сумы',
          'Суоярви', 'Сурабая', 'Сураж', 'Сурат', 'Сургут', 'Суровикино', 'Сурск', 'Сусуман', 'Сухиничи',
          'Сухой Лог', 'Сухум', 'Сходня', 'Сызрань', 'Сыктывкар', 'Сысерть', 'Сычёвка', 'Сянган',
          'Сясьстрой', 'Тавда', 'Таганрог', 'Тайбэй', 'Тайга', 'Тайшет', 'Тайюань', 'Талас', 'Талдом', 'Талица',
          'Таллин', 'Талнах', 'Тамбов', 'Тампере', 'Таншань', 'Тара', 'Тарко-Сале', 'Тарту', 'Таруса',
          'Татарск', 'Ташкент', 'Таштагол', 'Тбилиси', 'Тверия', 'Тверь', 'Теберда', 'Тебриз', 'Тегеран', 'Тейково',
          'Тель-Авив', 'Темников', 'Темрюк', 'Терек', 'Тернополь', 'Тетюши', 'Тилбург', 'Тимашёвск', 'Тирасполь',
          'Тихвин', 'Тихорецк', 'Тобольск', 'Тогучин', 'Токио', 'Токмак', 'Тольятти', 'Томари', 'Томмот', 'Томск',
          'Топки', 'Торжок', 'Торонто', 'Торопец', 'Тосно', 'Тотьма', 'Трёхгорный', 'Троицк', 'Троицк', 'Тромсё',
          'Тронхейм', 'Трубчевск', 'Туапсе', 'Туймазы', 'Тула', 'Тулуза', 'Тулун', 'Туран', 'Туринск', 'Тутаев',
          'Тында', 'Тырныауз', 'Тэгу', 'Тэджон', 'Тюкалинск', 'Тюмень', 'Тяньцзинь', 'Уварово', 'Углегорск',
          'Углич', 'Удачный', 'Удомля', 'Ужгород', 'Ужур', 'Узловая', 'Улан-Удэ', 'Ульяновск', 'Унеча', 'Урай',
          'Ургенч', 'Урень', 'Уржум', 'Урумчи', 'Урус-Мартан', 'Урюпинск', 'Усинск', 'Усмань', 'Усолье',
          'Усолье-Сибирское', 'Уссурийск', 'Усть-Джегута', 'Усть-Илимск', 'Усть-Катав', 'Усть-Кут', 'Усть-Лабинск',
          'Устюжна', 'Утрехт', 'Уфа', 'Ухань', 'Ухта', 'Учалы', 'Учкудук', 'Уяр', 'Фатеж', 'Фейсалабад', 'Феодосия',
          'Филадельфия', 'Финикс', 'Флоренция', 'Фокино', 'Франкфурт-на-Майне', 'Франкфурт-на-Одере', 'Фролово',
          'Фромборк', 'Фрязино', 'Фукуока', 'Фурманов', 'Фушунь', 'Хабаровск', 'Хадера', 'Хадыженск', 'Хайдерабад',
          'Хайфа', 'Хайфон', 'Халеб', 'Ханой', 'Ханты-Мансийск', 'Ханчжоу', 'Харабали', 'Хараре', 'Харбин',
          'Харлем', 'Харовск', 'Харьков', 'Хасавюрт', 'Хелдер', 'Хеврон', 'Хельсинки', 'Херсон', 'Хертогенбос',
          'Хвалынск', 'Хилок', 'Химки', 'Хиросима', 'Хмельницкий', 'Холм', 'Холмск', 'Холон', 'Хотьково', 'Хошимин',
          'Хьюстон', 'Цзинань', 'Цфат', 'Цхинвал', 'Цивильск', 'Цзыбо', 'Цюрих', 'Цимлянск', 'Цимлянск', 'Цзюлун',
          'Цицикар', 'Цукуба', 'Циндао', 'Чадан', 'Чайковский', 'Чанша', 'Чаньчунь', 'Чапаевск', 'Чаплыгин',
          'Чебаркуль', 'Чебоксары', 'Чегем', 'Чекалин', 'Челябинск', 'Чердынь', 'Черемхово', 'Черепаново',
          'Череповец', 'Черкассы', 'Черкесск', 'Чермоз', 'Чернигов', 'Черновцы', 'Черноголовка', 'Черногорск',
          'Чернушка', 'Черняховск', 'Чехов', 'Чикаго', 'Чистополь', 'Чита', 'Читтагонг', 'Чкаловск', 'Чолпон-Ата',
          'Чудово', 'Чулым', 'Чунцин', 'Чусовой', 'Чухлома', 'Чэнду', 'Шагонар', 'Шадринск', 'Шали', 'Шанхай',
          'Шарджа', 'Шарлеруа', 'Шартр', 'Шарыпово', 'Шарья', 'Шатки', 'Шатура', 'Шахтёрск', 'Шахты', 'Шахунья',
          'Шацк', 'Шверин', 'Шебекино', 'Шевченко', 'Шелехов', 'Шенкурск', 'Шеффилд', 'Шилка', 'Шимановск',
          'Шиханы', 'Шклов', 'Шлиссельбург', 'Штутгарт', 'Шумерля', 'Шумиха', 'Шуя', 'Шымкент', 'Шэньян',
          'Щербинка', 'Щецин', 'Щёкино', 'Щёлково', 'Щигры', 'Щучинск', 'Щучье', 'Эйлат', 'Эйндховен',
          'Электрогорск', 'Электросталь', 'Электроугли', 'Элиста', 'Эль-Гиза', 'Эль-Кувейт', 'Энгельс', 'Энсхеде',
          'Эр-Рияд', 'Эртиль', 'Эрфурт', 'Эсберг', 'Эспоо', 'Эссен', 'Юбилейный', 'Югорск', 'Южа', 'Южно-Сахалинск',
          'Южно-Сухокумск', 'Южноуральск', 'Юрга', 'Юрмала', 'Юрьев-Польский', 'Юрьевец', 'Юрюзань', 'Юхнов',
          'Ядрин', 'Якутск', 'Ялта', 'Ялуторовск', 'Янаул', 'Янгон', 'Яранск', 'Яровое', 'Ярославль', 'Ярцево',
          'Ясногорск', 'Ясный', 'Яхрома']

array_city = cities

a_city = ['й', 'ь']

bot_type = False
error_user_word = []

array_hp = [{"ход": 0, "user_xp": 10, "bot_xp": 10}]
user_xp = []
bot_xp = []

array_fifteen = [{'id': '1', 'age': '16', 'gender': 'm', 'login': 'Вася'},
                 {'id': '2', 'age': '18', 'gender': 'm', 'login': 'Петя'},
                 {'id': '3', 'age': '20', 'gender': 'g', 'login': 'Катя'},
                 {'id': '4', 'age': '20', 'gender': 'm', 'login': 'Стас'},
                 {'id': '5', 'age': '12', 'gender': 'g', 'login': 'Маша'},
                 {'id': '6', 'age': '44', 'gender': 'g', 'login': 'Галя'},
                 {'id': '7', 'age': '45', 'gender': 'm', 'login': 'Макс'},
                 {'id': '8', 'age': '20', 'gender': 'm', 'login': 'Илья'},
                 {'id': '9', 'age': '20', 'gender': 'g', 'login': 'Даша'},]