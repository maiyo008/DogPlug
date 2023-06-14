-- MySQL dump 10.13  Distrib 8.0.33, for Linux (x86_64)
--
-- Host: localhost    Database: dogplug_dev_db
-- ------------------------------------------------------
-- Server version	8.0.33-0ubuntu0.20.04.2

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `counties`
--

DROP TABLE IF EXISTS `counties`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `counties` (
  `name` varchar(100) NOT NULL,
  `id` varchar(40) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `counties`
--

LOCK TABLES `counties` WRITE;
/*!40000 ALTER TABLE `counties` DISABLE KEYS */;
INSERT INTO `counties` VALUES ('Malindi','6faa9c56-28ee-4aaa-b67b-44ae1b9f5afc','2023-05-31 18:09:49','2023-05-31 18:09:49'),('Kajiado','aa9637d7-c806-4b1f-b15b-ce0772972426','2023-06-05 02:39:31','2023-06-05 02:39:31'),('Mandera','b1c2d3e4f5g6h7i8j9k0l1m2n3o4p5','2022-01-10 15:30:45','2023-08-10 20:45:30'),('Machakos','d620617b-ce81-4fa1-be09-bb7ce950b465','2023-06-05 03:11:34','2023-06-05 03:11:34'),('Kiambu','g1h2i3j4k5l6m7n8o9p0q1r2s3t4u5','2022-01-16 16:45:00','2023-09-22 06:00:00'),('Baringo','n1o2p3q4r5s6t7u8v9w0x1y2z3a4b5','2022-01-19 19:19:19','2023-04-20 16:20:00'),('Meru','o1p2q3r4s5t6u7v8w9x0y1z2a3b4c5','2022-01-30 12:00:00','2025-06-15 10:30:15'),('Wajir','p1q2r3s4t5u6v7w8x9y0z1a2b3c4d5','2022-01-07 19:30:00','2023-12-25 08:00:00'),('Marsabit','s1t2u3v4w5x6y7z8a9b0c1d2e3f4g5','2022-01-10 15:30:45','2023-12-25 08:00:00'),('Kiambu','u1v2w3x4y5z6a7b8c9d0e1f2g3h4i5','2022-01-28 09:30:00','2023-11-11 11:11:11'),('Machakos','v1w2x3y4z5a6b7c8d9e0f1g2h3i4j5','2022-01-04 23:59:59','2025-05-31 18:09:49');
/*!40000 ALTER TABLE `counties` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dogs`
--

DROP TABLE IF EXISTS `dogs`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `dogs` (
  `name` varchar(40) NOT NULL,
  `breed` varchar(40) NOT NULL,
  `weight` int NOT NULL,
  `age` int NOT NULL,
  `owner_id` varchar(40) NOT NULL,
  `id` varchar(40) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `owner_id` (`owner_id`),
  CONSTRAINT `dogs_ibfk_1` FOREIGN KEY (`owner_id`) REFERENCES `owners` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dogs`
--

LOCK TABLES `dogs` WRITE;
/*!40000 ALTER TABLE `dogs` DISABLE KEYS */;
INSERT INTO `dogs` VALUES ('Warren','Hybrid',5,12,'fc5894fb-2e61-45ae-b9ac-31c0d1122078','02fb8ebd-5e8d-4120-8c7f-a77bc36466ba','2023-06-09 10:19:54','2023-06-09 10:19:54'),('Chiwawa','\"German',21,3,'bc3a5278-ff8c-4658-9877-ecceeb4b6d3d','312d9ee8-7e95-4ff3-b6c5-93e45d556857','2023-06-01 09:50:05','2023-06-01 09:50:05'),('Chiwawa','\"German',21,3,'bc3a5278-ff8c-4658-9877-ecceeb4b6d3d','59467f09-96e7-466c-8302-484c85174a32','2023-06-01 09:48:57','2023-06-01 09:48:57'),('Chiwawa','\"German',21,3,'bc3a5278-ff8c-4658-9877-ecceeb4b6d3d','6a2698bc-c522-4052-ab4b-4afb8d7ae967','2023-06-01 09:47:57','2023-06-01 09:47:57'),('Chiwawa','Germanshepherd',21,3,'bc3a5278-ff8c-4658-9877-ecceeb4b6d3d','6a7dd474-e6f5-49da-a932-a26de5394c06','2023-06-01 09:50:57','2023-06-01 09:50:57'),('Chui','German sherpherd',22,30,'e28127f4-3164-4dcb-9e92-aed571a089a7','79a7d907-d8df-4df1-8d6e-a203bcafc6c7','2023-06-09 10:41:53','2023-06-09 10:41:53'),('Toby','Staffordshire Bull Terrier',10,5,'1j4k2l3m-5n8b6v7c-9x0z1a2s3d4f5g6h','9012ff98-1bbb-7www-vpn5-55bb1c2d3qrs','2022-01-30 12:00:00','2025-05-31 18:09:49'),('Simba','Bulldog',40,5,'2f1e3d4c-5b6a-7d8c-9e0f-a1b2c3d4e5f6','9012ff98-1ddd-6www-vpn5-55bb1c2d3qrs','2022-01-13 12:34:56','2024-01-01 00:00:00'),('Hank','Pomeranian',10,5,'1a2b3c4d-5e6f7g8h-9i0j1k2l3m4n5o6p','9012ff98-1jjj-6www-vpn5-55bb1c2d3qrs','2022-01-10 15:30:45','2025-05-31 18:09:49'),('Ruby','Basset Hound',22,8,'1j2k3l4m-5n6b7v8c-9x0z1a2s3d4f5g6h','9012ff98-1ppp-6www-vpn5-55bb1c2d3qrs','2022-01-07 19:30:00','2025-06-15 10:30:15'),('Marley','Bichon Frise',33,5,'2j4k1l3m-6n8b5v7c-0x9z1a8s2d4f3g6h','9012ff98-1vvv-6www-vpn5-55bb1c2d3qrs','2022-01-14 18:00:00','2024-09-22 06:00:00'),('Rocky','Cocker Spaniel',40,5,'6faa9c56-28ee-4aaa-b67b-44ae1b9f5afc','9123ff98-1aaa-6www-vpn5-55bb1c2d3qrs','2022-01-21 13:13:13','2023-11-11 11:11:11'),('Bailey','Whippet',40,6,'5a4b3c2d-1e2f-3g4h-5i6j-7k8l9m0n1o2','9123ff98-1ggg-6www-vpn5-55bb1c2d3qrs','2022-01-22 23:59:59','2024-01-01 00:00:00'),('Toby','French Bulldog',22,5,'9q8w7e6r-5t4y3u2i-1o2p3a4s5d6f7g8h','9123ff98-1mmm-6www-vpn5-55bb1c2d3qrs','2022-01-25 11:11:11','2025-02-14 12:30:45'),('Riley','Australian Shepherd',25,5,'8q5w6e3r-4t7y2u9i-0o1p8a6s5d2f3g4h','9123ff98-1sss-6www-vpn5-55bb1c2d3qrs','2022-01-03 17:45:30','2024-08-10 20:45:30'),('Jack','Afghan Hound',25,5,'7q5w2e3r-3t8y9u6i-0o1p4a6s5d2f3g4h','9123ff98-1yyy-6www-vpn5-55bb1c2d3qrs','2022-01-11 09:00:00','2023-06-15 10:30:15'),('Bailey','Poodle',25,5,'c3b2a1d4-5f6a-4b8e-9c7d-8e3f2a1b0d9f','9345ff98-1bbb-6www-vpn5-55bb1c2d3qrs','2022-01-28 09:30:00','2024-07-04 14:00:00'),('Roxy','Newfoundland',25,6,'9p8o7i6u-5y4t3r2e-1w2q1a2s3d4f5g6h','9345ff98-1hhh-6www-vpn5-55bb1c2d3qrs','2022-01-02 08:30:15','2023-09-22 06:00:00'),('Lucy','Poodle',30,5,'2j3k4l5m-6n7b8v9c-0x1z2a3s4d5f6g7h','9345ff98-1nnn-6www-vpn5-55bb1c2d3qrs','2022-01-30 12:00:00','2025-04-20 16:20:00'),('Charlie','French Bulldog',30,5,'1j4k2l3m-5n8b6v7c-9x0z1a2s3d4f5g6h','9345ff98-1ttt-6www-vpn5-55bb1c2d3qrs','2022-01-10 15:30:45','2023-11-11 11:11:11'),('Bentley','Rottweiler',30,6,'2j4k3l1m-6n8b5v9c-0x9z1a8s2d4f3g6h','9345ff98-1zzz-6www-vpn5-55bb1c2d3qrs','2022-01-19 19:19:19','2025-05-31 18:09:49'),('Chloe','Beagle',25,6,'9a8b7c6d-5e4f-3a2b-1c0d-f9e8d7c6b5a4','9456ff98-1eee-6www-vpn5-55bb1c2d3qrs','2022-01-06 14:20:00','2025-02-14 12:30:45'),('Molly','Chinese Shar-Pei',25,5,'7q8w9e0r-1t2y3u4i-5o6p7a8s9d0f1g2h','9456ff98-1kkk-6www-vpn5-55bb1c2d3qrs','2022-01-29 20:20:20','2023-09-22 06:00:00'),('Harley','Doberman Pinscher',25,5,'7q6w5e4r-3t2y1u0i-9o8p7a6s5d4f3g2h','9456ff98-1qqq-6www-vpn5-55bb1c2d3qrs','2022-01-06 14:20:00','2025-01-01 00:00:00'),('Winston','Bulldog',40,5,'8q5w4e3r-4t7y6u9i-0o1p2a6s5d8f3g4h','9456ff98-1www-6www-vpn5-55bb1c2d3qrs','2022-01-05 06:15:45','2024-01-01 00:00:00'),('Buddy','Yorkshire Terrier',25,5,'8q5w4e2r-4t7y6u9i-0o1p3a6s5d8f3g4h','9678ff98-1aaa-7www-vpn5-55bb1c2d3qrs','2022-01-09 22:22:22','2024-05-31 18:09:49'),('Sophie','Poodle',40,5,'8d9e1c2b-7a6f-4e5d-bc8c-3f4a5e6d7b8a','9678ff98-1ccc-6www-vpn5-55bb1c2d3qrs','2022-01-13 12:34:56','2025-03-05 08:15:30'),('Bentley','Jack Russell Terrier',20,5,'7j6k5l4m-3n2o1p0q-9r8s7t6u5v4w3x2y','9678ff98-1iii-6www-vpn5-55bb1c2d3qrs','2022-01-05 06:15:45','2025-05-31 18:09:49'),('Lola','Siberian Husky',22,6,'8q7w6e5r-4t3y2u1i-0o9p8a7s6d5f4g3h','9678ff98-1ooo-6www-vpn5-55bb1c2d3qrs','2022-01-20 08:00:00','2024-01-01 00:00:00'),('Gus','Whippet',10,5,'7q5w6e2r-3t8y4u9i-0o1p7a6s2d5f3g4h','9678ff98-1uuu-6www-vpn5-55bb1c2d3qrs','2022-01-14 18:00:00','2024-05-31 18:09:49'),('Penny','Basset Hound',40,5,'1b2c3d4e-5f6a-7b8c-9d0e-a1b2c3d4e5f6','9789ff98-1fff-6www-vpn5-55bb1c2d3qrs','2022-01-12 20:20:20','2024-03-05 08:15:30'),('Lily','Chinese Shar-Pei',25,5,'3j4k5l6m-7n8b9v0c-1x2z3a4s5d6f7g8h','9789ff98-1lll-6www-vpn5-55bb1c2d3qrs','2022-01-10 15:30:45','2023-12-25 08:00:00'),('Jack','Yorkshire Terrier',25,5,'2j1k4l3m-6n5b8v7c-0x9z1a8s2d7f3g6h','9789ff98-1rrr-6www-vpn5-55bb1c2d3qrs','2022-01-15 07:30:00','2024-10-31 23:59:59'),('Bailey','Australian Shepherd',25,6,'1j4k3l2m-5n8b7v6c-9x0z1a2s3d4f5g6h','9789ff98-1xxx-6www-vpn5-55bb1c2d3qrs','2022-01-25 11:11:11','2024-05-31 18:09:49'),('Rex','Doberman',26,10,'256f979b-a358-4e61-b6d2-bd67c1dcb622','da8e8561-a71b-421f-8017-be7bd8631f77','2023-06-10 17:34:20','2023-06-10 17:34:20');
/*!40000 ALTER TABLE `dogs` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `groomers`
--

DROP TABLE IF EXISTS `groomers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `groomers` (
  `name` varchar(100) NOT NULL,
  `email` varchar(30) NOT NULL,
  `contact` varchar(30) NOT NULL,
  `id` varchar(40) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `groomers`
--

LOCK TABLES `groomers` WRITE;
/*!40000 ALTER TABLE `groomers` DISABLE KEYS */;
INSERT INTO `groomers` VALUES ('Olivia Williams','selena.gomez@example.com','254778901235','1dddgg12-9iii-7ddd-ppp7-88aa4c5d6klm','2022-01-20 08:00:00','2024-04-20 16:20:00'),('Ava Davis','harry.styles@example.com','254745678901','1qqqaa12-8hhh-5rrr-ppp6-22dd4e5f9mno','2022-01-17 21:00:00','2025-02-14 12:30:45'),('Charlotte Perez','jane.smith@example.com','254799999999','1wwwbb12-4uuu-6ddd-ppp7-77aa3c4d5klm','2022-01-08 11:11:11','2024-11-11 11:11:11'),('Emily Nelson','kendrick.lamar@example.com','254711111111','1zzzbb12-6uuu-3ddd-ppp7-66cc3a4b5ijk','2022-01-06 14:20:00','2023-06-15 10:30:15'),('Michael Edwards','katy.perry@example.com','254788888888','2dddff23-9iii-5zzz-bbn8-88cc1a2b3hij','2022-01-21 13:13:13','2023-01-01 00:00:00'),('Isabella Hernandez','ariana.grande@example.com','254701234567','2pppaa23-4hhh-5rrr-lll9-88dd5e6f7fgh','2022-01-06 14:20:00','2024-09-22 06:00:00'),('Mason Perez','bruce.springsteen@example.com','254723456789','2sddff23-9iii-1zzz-bbn8-44cc1a2b9hgf','2022-01-09 22:22:22','2025-01-01 00:00:00'),('Michael Edwards','eminem@example.com','254767890124','2zzzff23-4uuu-8zzz-bbn8-77cc1a3b2hij','2022-01-24 18:45:00','2024-12-25 08:00:00'),('Lucas Lopez','david.bowie@example.com','254789012345','3jjjdd34-5iii-6ddd-ooo4-33cc6a7b8zab','2022-01-04 23:59:59','2023-12-25 08:00:00'),('Ethan Garcia','eminem@example.com','254766666666','3rrraa34-7hhh-2rrr-ooo8-11dd0e1f2xyz','2022-01-29 20:20:20','2024-03-05 08:15:30'),('Amelia Flores','cardi.b@example.com','254745678902','3rrrdd34-2iii-2rrr-ooo8-44aa0e1f2zab','2022-01-27 16:00:00','2024-04-20 16:20:00'),('Charlotte Perez','eminem@example.com','254744444444','4hhhgg45-3uuu-4yyy-ccc2-22aa8b9c0rst','2022-01-12 20:20:20','2024-12-25 08:00:00'),('Michael Edwards','justin.bieber@example.com','254701234568','4pppbb45-5hhh-3yyy-ccc2-33ee8a9b1tuv','2022-01-08 11:11:11','2023-07-04 14:00:00'),('Isaac Wood','david.bowie@example.com','254767890123','4rrrff45-2uuu-7zzz-ccc2-99bb8c7d3stu','2022-01-07 19:30:00','2024-11-11 11:11:11'),('Mia Gonzalez','eminem@example.com','254723456780','4zzzgg45-1hhh-4yyy-ccc2-66ee8a9b0tuv','2022-01-09 22:22:22','2024-11-11 11:11:11'),('Safisha','safisha@gmail.com','0123456789','5b01bdef-da2c-4831-a6f4-305698e12a0b','2023-06-01 10:00:25','2023-06-01 10:00:25'),('Harper Cruz','rihanna@example.com','254722222222','5dddff56-8iii-1www-kkl4-99bb2c3d6lmn','2022-01-03 17:45:30','2023-04-20 16:20:00'),('Mason Perez','lady.gaga@example.com','254734567890','5ttggh56-6ppp-2ddd-kkl9-88vv5b3c6jkl','2022-01-12 20:20:20','2023-08-10 20:45:30'),('Benjamin Parker','drake@example.com','254789012346','5wwwyy56-3ppp-1zzz-kkl9-66dd2e3f4nop','2022-01-22 23:59:59','2023-10-31 23:59:59'),('Daniel Cooper','john.doe@example.com','254700000000','5yyytt56-2iii-1zzz-kkl9-99dd2e3f4nop','2022-01-30 12:00:00','2024-06-15 10:30:15'),('Aria Reed','selena.gomez@example.com','254778901234','6tttyy67-1ppp-8www-fff3-11aa9b2c5vwx','2022-01-07 19:30:00','2025-02-14 12:30:45'),('Isaac Wood','post.malone@example.com','254756789013','6wwwtt67-8hhh-5ddd-lll3-11bb9c2d4efg','2022-01-17 21:00:00','2025-06-15 10:30:15'),('Addison Ross','david.bowie@example.com','254777777777','6zzzdd67-5ppp-8www-lll3-33bb9c1d4efg','2022-01-04 23:59:59','2023-11-11 11:11:11'),('Benjamin Parker','adele@example.com','254790123456','7uuukk78-9zzz-2yyy-rrr1-55ee0f1g2cde','2022-01-22 23:59:59','2024-12-25 08:00:00'),('Daniel Cooper','amy.winehouse@example.com','254734567891','8dddyy78-6ppp-9www-fff6-33cc5b6c7wxy','2022-01-18 10:10:10','2024-05-31 18:09:49'),('Noah Brown','chris.brown@example.com','254712345678','8swwyy78-4uuu-3www-vpn7-66wx3z1a7yws','2022-01-18 10:10:10','2023-08-10 20:45:30'),('Addison Ross','cardi.b@example.com','254755555555','8wwwyy78-1iii-9ddd-fff6-44cc5a6b7uvw','2022-01-25 11:11:11','2024-11-11 11:11:11'),('Abigail Mitchell','adele@example.com','254712345679','9pppff98-3uuu-7www-vpn5-22bb1c2d4qrs','2022-01-14 18:00:00','2025-03-05 08:15:30'),('Alexander Scott','selena.gomez@example.com','254756789012','9wwwee98-3jjj-4yyy-lll5-77aa2b1c4pqr','2022-01-13 12:34:56','2023-12-25 08:00:00'),('Olivia Williams','justin.bieber@example.com','254790123457','9yyyff98-1uuu-6www-vpn5-55bb1c2d3qrs','2022-01-25 11:11:11','2024-02-14 12:30:45'),('Jacob Torres','lady.gaga@example.com','254733333333','9yyytt98-2ppp-7zzz-vpn5-77ee1b2c4opq','2022-01-07 19:30:00','2024-01-01 00:00:00');
/*!40000 ALTER TABLE `groomers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `locations`
--

DROP TABLE IF EXISTS `locations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `locations` (
  `longitude` varchar(40) DEFAULT NULL,
  `latitude` varchar(40) DEFAULT NULL,
  `groomer_id` varchar(40) NOT NULL,
  `town_id` varchar(40) NOT NULL,
  `id` varchar(40) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `groomer_id` (`groomer_id`),
  KEY `town_id` (`town_id`),
  CONSTRAINT `locations_ibfk_1` FOREIGN KEY (`groomer_id`) REFERENCES `groomers` (`id`),
  CONSTRAINT `locations_ibfk_2` FOREIGN KEY (`town_id`) REFERENCES `towns` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `locations`
--

LOCK TABLES `locations` WRITE;
/*!40000 ALTER TABLE `locations` DISABLE KEYS */;
INSERT INTO `locations` VALUES ('','','5b01bdef-da2c-4831-a6f4-305698e12a0b','2492bd46-be18-4f7d-8783-85fe46b22677','5d079351-deeb-4a31-b725-db3c45c2bc67','2023-06-01 11:16:45','2023-06-01 11:16:45'),('-43.1729','37.7749','5dddff56-8iii-1www-kkl4-99bb2c3d6lmn','bb9637d7-c806-4b1f-b15b-ce0772972426','a1b2c3d4-e5f6-7g8h-9i10-jk11lm12no13','2022-01-27 16:00:00','2023-03-05 08:15:30'),('100.5018','51.5074','1dddgg12-9iii-7ddd-ppp7-88aa4c5d6klm','aa9637d7-c806-4b1f-b15b-ce0772972426','d620617b-ce81-4fa1-be09-bb7ce950b465','2022-01-22 23:59:59','2024-01-01 00:00:00'),('-43.1729','55.7558','2sddff23-9iii-1zzz-bbn8-44cc1a2b9hgf','bb9637d7-c806-4b1f-b15b-ce0772972426','f1e2d3c4-b5a6-7d8c-9b10-a1f2e3d4c5b6','2022-01-11 09:00:00','2025-02-14 12:30:45');
/*!40000 ALTER TABLE `locations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `owners`
--

DROP TABLE IF EXISTS `owners`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `owners` (
  `name` varchar(100) NOT NULL,
  `email` varchar(40) NOT NULL,
  `contact` varchar(20) NOT NULL,
  `id` varchar(40) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `owners`
--

LOCK TABLES `owners` WRITE;
/*!40000 ALTER TABLE `owners` DISABLE KEYS */;
INSERT INTO `owners` VALUES ('Matthew Martinez','lady.gaga@example.com','254701234567','1a2b3c4d-5e6f7g8h-9i0j1k2l3m4n5o6p','2022-01-28 09:30:00','2024-08-10 20:45:30'),('Roy Orenge','royorenge@gmail.com','0726937957','1adf790a-4c60-402c-b21b-3216376ed712','2023-06-09 09:56:47','2023-06-09 09:56:47'),('Emily Davis','ed.sheeran@example.com','254767890123','1b2c3d4e-5f6a-7b8c-9d0e-a1b2c3d4e5f6','2022-01-19 19:19:19','2024-03-05 08:15:30'),('Roy Orenge','royorenge@gmail.com','0726937957','1f293226-0b3b-4e63-b608-02c1eb453f97','2023-06-09 09:54:03','2023-06-09 09:54:03'),('Christopher Wilson','john.doe@example.com','254766666666','1j2k3l4m-5n6b7v8c-9x0z1a2s3d4f5g6h','2022-01-12 20:20:20','2025-05-31 18:09:49'),('Jennifer Anderson','ariana.grande@example.com','254700000000','1j4k2l3m-5n8b6v7c-9x0z1a2s3d4f5g6h','2022-01-16 16:45:00','2023-05-31 18:09:49'),('Matthew Martinez','adele@example.com','254745678902','1j4k3l2m-5n8b7v6c-9x0z1a2s3d4f5g6h','2022-01-06 14:20:00','2025-03-05 08:15:30'),('Muthee Mumbi','mutheemumbi01@gmail.com','0718582605','256f979b-a358-4e61-b6d2-bd67c1dcb622','2023-06-10 17:34:20','2023-06-10 17:34:20'),('Emily Davis','taylor.swift@example.com','254745678901','2f1e3d4c-5b6a-7d8c-9e0f-a1b2c3d4e5f6','2022-01-13 12:34:56','2024-03-05 08:15:30'),('Sarah Lee','chris.brown@example.com','254788888888','2j1k4l3m-6n5b8v7c-0x9z1a8s2d7f3g6h','2022-01-17 21:00:00','2024-09-22 06:00:00'),('Matthew Martinez','travis.scott@example.com','254744444444','2j3k4l5m-6n7b8v9c-0x1z2a3s4d5f6g7h','2022-01-10 15:30:45','2023-12-25 08:00:00'),('Christopher Wilson','travis.scott@example.com','254723456780','2j4k1l3m-6n8b5v7c-0x9z1a8s2d4f3g6h','2022-01-17 21:00:00','2024-06-15 10:30:15'),('John Smith','justin.bieber@example.com','254767890124','2j4k3l1m-6n8b5v9c-0x9z1a8s2d4f3g6h','2022-01-05 06:15:45','2023-06-15 10:30:15'),('Amanda Taylor','jennifer.lee@example.com','254722222222','3j4k5l6m-7n8b9v0c-1x2z3a4s5d6f7g8h','2022-01-04 23:59:59','2023-06-15 10:30:15'),('Christopher Wilson','shawn.mendes@example.com','254778901234','5a4b3c2d-1e2f-3g4h-5i6j-7k8l9m0n1o2','2022-01-20 08:00:00','2023-11-11 11:11:11'),('Christopher Wilson','lady.gaga@example.com','254712345678','6faa9c56-28ee-4aaa-b67b-44ae1b9f5afc','2022-01-07 19:30:00','2025-06-15 10:30:15'),('Roy Orenge','royorenge@gmail.com','0726937957','77936e29-0b8e-4a94-8a84-1633b73020b5','2023-06-09 09:55:59','2023-06-09 09:55:59'),('Jessica Brown','chris.brown@example.com','254790123456','7j6k5l4m-3n2o1p0q-9r8s7t6u5v4w3x2y','2022-01-20 08:00:00','2023-09-22 06:00:00'),('Jennifer Anderson','eminem@example.com','254756789013','7q5w2e3r-3t8y9u6i-0o1p4a6s5d2f3g4h','2022-01-20 08:00:00','2024-02-14 12:30:45'),('Amanda Taylor','jennifer.lee@example.com','254712345679','7q5w6e2r-3t8y4u9i-0o1p7a6s2d5f3g4h','2022-01-25 11:11:11','2025-02-14 12:30:45'),('Michael Johnson','mariah.carey@example.com','254777777777','7q6w5e4r-3t2y1u0i-9o8p7a6s5d4f3g2h','2022-01-15 07:30:00','2023-05-31 18:09:49'),('Jennifer Anderson','ed.sheeran@example.com','254711111111','7q8w9e0r-1t2y3u4i-5o6p7a8s9d0f1g2h','2022-01-21 13:13:13','2024-10-31 23:59:59'),('Jennifer Anderson','mariah.carey@example.com','254734567890','8d9e1c2b-7a6f-4e5d-bc8c-3f4a5e6d7b8a','2022-01-20 08:00:00','2023-12-25 08:00:00'),('David Rodriguez','justin.bieber@example.com','254778901235','8q5w4e2r-4t7y6u9i-0o1p3a6s5d8f3g4h','2022-01-17 21:00:00','2023-02-14 12:30:45'),('David Rodriguez','shawn.mendes@example.com','254734567891','8q5w4e3r-4t7y6u9i-0o1p2a6s5d8f3g4h','2022-01-01 12:00:00','2023-10-31 23:59:59'),('Jennifer Anderson','justin.bieber@example.com','254799999999','8q5w6e3r-4t7y2u9i-0o1p8a6s5d2f3g4h','2022-01-15 07:30:00','2023-11-11 11:11:11'),('Sarah Lee','beyonce@example.com','254755555555','8q7w6e5r-4t3y2u1i-0o9p8a7s6d5f4g3h','2022-01-14 18:00:00','2023-07-04 14:00:00'),('David Rodriguez','travis.scott@example.com','254756789012','9a8b7c6d-5e4f-3a2b-1c0d-f9e8d7c6b5a4','2022-01-16 16:45:00','2024-04-20 16:20:00'),('Amanda Taylor','jennifer.lee@example.com','254789012345','9p8o7i6u-5y4t3r2e-1w2q1a2s3d4f5g6h','2022-01-23 14:30:00','2024-01-01 00:00:00'),('Sarah Lee','chris.brown@example.com','254733333333','9q8w7e6r-5t4y3u2i-1o2p3a4s5d6f7g8h','2022-01-23 14:30:00','2023-09-22 06:00:00'),('Simba','simba@gmail.com','07123456789','bc3a5278-ff8c-4658-9877-ecceeb4b6d3d','2023-06-01 09:33:33','2023-06-01 09:33:33'),('Ay','ay@gmail.com','0726937952','bc430f4f-440b-450c-a868-2a5273fc117e','2023-06-09 09:57:44','2023-06-09 09:57:44'),('David Rodriguez','rihanna@example.com','254723456789','c3b2a1d4-5f6a-4b8e-9c7d-8e3f2a1b0d9f','2022-01-04 23:59:59','2023-03-05 08:15:30'),('Michael Owen','owen@gmail.com','014578963','e28127f4-3164-4dcb-9e92-aed571a089a7','2023-06-09 10:41:53','2023-06-09 10:41:53'),('Tony Kipruto Maiyo','tonymaiyo008@gmail.com','0726937955','f998e983-df0a-400f-86fc-fcb24bca030b','2023-06-09 09:37:51','2023-06-09 09:37:51'),('abc xyz','abcxyz@gmailc.com','0712648945','fc5894fb-2e61-45ae-b9ac-31c0d1122078','2023-06-09 10:19:54','2023-06-09 10:19:54');
/*!40000 ALTER TABLE `owners` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `reviews`
--

DROP TABLE IF EXISTS `reviews`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `reviews` (
  `description` varchar(256) DEFAULT NULL,
  `star_rating` int DEFAULT NULL,
  `owner_id` varchar(40) NOT NULL,
  `groomer_id` varchar(40) NOT NULL,
  `id` varchar(40) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `owner_id` (`owner_id`),
  KEY `groomer_id` (`groomer_id`),
  CONSTRAINT `reviews_ibfk_1` FOREIGN KEY (`owner_id`) REFERENCES `owners` (`id`),
  CONSTRAINT `reviews_ibfk_2` FOREIGN KEY (`groomer_id`) REFERENCES `groomers` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `reviews`
--

LOCK TABLES `reviews` WRITE;
/*!40000 ALTER TABLE `reviews` DISABLE KEYS */;
INSERT INTO `reviews` VALUES ('The groomer did a great job',5,'bc3a5278-ff8c-4658-9877-ecceeb4b6d3d','5b01bdef-da2c-4831-a6f4-305698e12a0b','5bafc999-965f-4552-9fd4-a1c8bd51f371','2023-06-01 10:18:20','2023-06-01 10:18:20'),('Pet chiropractic',6,'6faa9c56-28ee-4aaa-b67b-44ae1b9f5afc','8swwyy78-4uuu-3www-vpn7-66wx3z1a7yws','9012ff98-1bbb-7www-vpn5-55bb1c2d3qrs','2022-01-29 20:20:20','2025-05-31 18:09:49'),('Ear cleaning',10,'1j4k2l3m-5n8b6v7c-9x0z1a2s3d4f5g6h','5wwwyy56-3ppp-1zzz-kkl9-66dd2e3f4nop','a0b1c2d3-4e5f-6g7h-8i9j-0k1l2m3n4o','2022-01-02 08:30:15','2023-03-05 08:15:30'),('Dog walking',1,'c3b2a1d4-5f6a-4b8e-9c7d-8e3f2a1b0d9f','2sddff23-9iii-1zzz-bbn8-44cc1a2b9hgf','a0d3f1c2-4e5f-6g7h-8i9j-0k1l2m3n4o5p','2022-01-27 16:00:00','2024-07-04 14:00:00'),('Cat grooming',6,'8d9e1c2b-7a6f-4e5d-bc8c-3f4a5e6d7b8a','5ttggh56-6ppp-2ddd-kkl9-88vv5b3c6jkl','b1c2d3e4-5f6g-7h8i-9j0k-1l2m3n4o5p6','2022-01-09 22:22:22','2024-02-14 12:30:45'),('Nail trimming and filing',3,'2f1e3d4c-5b6a-7d8c-9e0f-a1b2c3d4e5f6','1qqqaa12-8hhh-5rrr-ppp6-22dd4e5f9mno','c2d3e4f5-6g7h-8i9j-0k1l-2m3n4o5p6q7','2022-01-06 14:20:00','2023-11-11 11:11:11'),('Pet training',5,'9a8b7c6d-5e4f-3a2b-1c0d-f9e8d7c6b5a4','9wwwee98-3jjj-4yyy-lll5-77aa2b1c4pqr','d3e4f5g6-7h8i-9j0k-1l2m-3n4o5p6q7r8','2022-01-21 13:13:13','2024-08-10 20:45:30'),('Pet product sales',8,'1b2c3d4e-5f6a-7b8c-9d0e-a1b2c3d4e5f6','4rrrff45-2uuu-7zzz-ccc2-99bb8c7d3stu','e4f5g6h7-8i9j-0k1l-2m3n-4o5p6q7r8s9','2022-01-27 16:00:00','2025-04-20 16:20:00'),('Pet daycare',5,'5a4b3c2d-1e2f-3g4h-5i6j-7k8l9m0n1o2','6tttyy67-1ppp-8www-fff3-11aa9b2c5vwx','f5g6h7i8-9j0k-1l2m-3n4o-5p6q7r8s9t','2022-01-06 14:20:00','2025-03-05 08:15:30'),('Ear piercing',9,'9p8o7i6u-5y4t3r2e-1w2q1a2s3d4f5g6h','3jjjdd34-5iii-6ddd-ooo4-33cc6a7b8zab','g6h7i8j9-0k1l-2m3n-4o5p-6q7r8s9t1u','2022-01-11 09:00:00','2024-05-31 18:09:49'),('Pet adoption services',2,'7j6k5l4m-3n2o1p0q-9r8s7t6u5v4w3x2y','7uuukk78-9zzz-2yyy-rrr1-55ee0f1g2cde','h7i8j9k0-1l2m-3n4o-5p6q-7r8s9t1u2v','2022-01-27 16:00:00','2023-09-22 06:00:00'),('Ear cleaning',4,'1a2b3c4d-5e6f7g8h-9i0j1k2l3m4n5o6p','2pppaa23-4hhh-5rrr-lll9-88dd5e6f7fgh','i8j9k0l1-2m3n-4o5p-6q7r-8s9t1u2v3w','2022-01-26 22:22:22','2024-02-14 12:30:45'),('Teeth whitening',5,'7q8w9e0r-1t2y3u4i-5o6p7a8s9d0f1g2h','1zzzbb12-6uuu-3ddd-ppp7-66cc3a4b5ijk','j9k0l1m2-3n4o-5p6q-7r8s-9t1u2v3w4x','2022-01-21 13:13:13','2024-11-11 11:11:11'),('Pet insurance',4,'3j4k5l6m-7n8b9v0c-1x2z3a4s5d6f7g8h','5dddff56-8iii-1www-kkl4-99bb2c3d6lmn','k0l1m2n3-4o5p-6q7r-8s9t-1u2v3w4x5y','2022-01-25 11:11:11','2024-10-31 23:59:59'),('Pet sitting',7,'9q8w7e6r-5t4y3u2i-1o2p3a4s5d6f7g8h','9yyytt98-2ppp-7zzz-vpn5-77ee1b2c4opq','l1m2n3o4-5p6q-7r8s-9t1u-2v3w4x5y6z','2022-01-27 16:00:00','2024-07-04 14:00:00'),('Pet training',2,'2j3k4l5m-6n7b8v9c-0x1z2a3s4d5f6g7h','4hhhgg45-3uuu-4yyy-ccc2-22aa8b9c0rst','m2n3o4p5-6q7r-8s9t-1u2v-3w4x5y6z0a','2022-01-26 22:22:22','2023-09-22 06:00:00'),('Full-service grooming',8,'8q7w6e5r-4t3y2u1i-0o9p8a7s6d5f4g3h','8wwwyy78-1iii-9ddd-fff6-44cc5a6b7uvw','n3o4p5q6-7r8s-9t1u-2v3w-4x5y6z0a1b','2022-01-28 09:30:00','2023-05-31 18:09:49'),('Ear piercing',9,'1j2k3l4m-5n6b7v8c-9x0z1a2s3d4f5g6h','3rrraa34-7hhh-2rrr-ooo8-11dd0e1f2xyz','o4p5q6r7-8s9t-1u2v-3w4x-5y6z0a1b2c','2022-01-30 12:00:00','2023-02-14 12:30:45'),('Pet transportation',9,'7q6w5e4r-3t2y1u0i-9o8p7a6s5d4f3g2h','6zzzdd67-5ppp-8www-lll3-33bb9c1d4efg','p5q6r7s8-9t1u-2v3w-4x5y-6z0a1b2c3d','2022-01-05 06:15:45','2023-04-20 16:20:00'),('Pet boarding',5,'2j1k4l3m-6n5b8v7c-0x9z1a8s2d7f3g6h','2dddff23-9iii-5zzz-bbn8-88cc1a2b3hij','q6r7s8t9-1u2v-3w4x-5y6z-0a1b2c3d4e','2022-01-07 19:30:00','2023-05-31 18:09:49'),('Full-service grooming',9,'8q5w6e3r-4t7y2u9i-0o1p8a6s5d2f3g4h','1wwwbb12-4uuu-6ddd-ppp7-77aa3c4d5klm','r7s8t9u1-2v3w-4x5y-6z0a-1b2c3d4e5f','2022-01-05 06:15:45','2024-04-20 16:20:00'),('Medicated bath',2,'1j4k2l3m-5n8b6v7c-9x0z1a2s3d4f5g6h','5yyytt56-2iii-1zzz-kkl9-99dd2e3f4nop','s8t9u1v2-3w4x-5y6z-0a1b-2c3d4e5f6g','2022-01-23 14:30:00','2024-11-11 11:11:11'),('Pet product sales',1,'7q5w6e2r-3t8y4u9i-0o1p7a6s2d5f3g4h','9pppff98-3uuu-7www-vpn5-22bb1c2d4qrs','t9u1v2w3-4x5y-6z0a-1b2c-3d4e5f6g7h','2022-01-03 17:45:30','2025-01-01 00:00:00'),('Pet training',7,'2j4k1l3m-6n8b5v7c-0x9z1a8s2d4f3g6h','4zzzgg45-1hhh-4yyy-ccc2-66ee8a9b0tuv','u1v2w3x4-5y6z-0a1b-2c3d-4e5f6g7h8i','2022-01-09 22:22:22','2024-09-22 06:00:00'),('Pet training',3,'8q5w4e3r-4t7y6u9i-0o1p2a6s5d8f3g4h','8dddyy78-6ppp-9www-fff6-33cc5b6c7wxy','v2w3x4y5-6z0a-1b2c-3d4e-5f6g7h8i9j','2022-01-16 16:45:00','2023-10-31 23:59:59'),('Pet adoption services',4,'1j4k3l2m-5n8b7v6c-9x0z1a2s3d4f5g6h','3rrrdd34-2iii-2rrr-ooo8-44aa0e1f2zab','w3x4y5z6-0a1b-2c3d-4e5f-6g7h8i9j0k','2022-01-06 14:20:00','2023-01-01 00:00:00'),('Pet chiropractic',9,'7q5w2e3r-3t8y9u6i-0o1p4a6s5d2f3g4h','6wwwtt67-8hhh-5ddd-lll3-11bb9c2d4efg','x4y5z6a0-1b2c-3d4e-5f6g-7h8i9j0k1l','2022-01-30 12:00:00','2025-05-31 18:09:49'),('Pet event planning',1,'2j4k3l1m-6n8b5v9c-0x9z1a8s2d4f3g6h','2zzzff23-4uuu-8zzz-bbn8-77cc1a3b2hij','y5z6a0b1-2c3d-4e5f-6g7h-8i9j0k1l2m','2022-01-11 09:00:00','2024-03-05 08:15:30'),('Dog walking',10,'8q5w4e2r-4t7y6u9i-0o1p3a6s5d8f3g4h','1dddgg12-9iii-7ddd-ppp7-88aa4c5d6klm','z6a0b1c2-3d4e-5f6g-7h8i-9j0k1l2m3n','2022-01-10 15:30:45','2023-02-14 12:30:45');
/*!40000 ALTER TABLE `reviews` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `services`
--

DROP TABLE IF EXISTS `services`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `services` (
  `description` varchar(256) NOT NULL,
  `duration` varchar(20) NOT NULL,
  `price` int NOT NULL,
  `groomer_id` varchar(40) NOT NULL,
  `id` varchar(40) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `groomer_id` (`groomer_id`),
  CONSTRAINT `services_ibfk_1` FOREIGN KEY (`groomer_id`) REFERENCES `groomers` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `services`
--

LOCK TABLES `services` WRITE;
/*!40000 ALTER TABLE `services` DISABLE KEYS */;
INSERT INTO `services` VALUES ('Skunk odor removal','4hrs',1900,'8swwyy78-4uuu-3www-vpn7-66wx3z1a7yws','a0d3f1c2-4e5f-6g7h-8i9j-0k1l2m3n4o5p','2022-01-06 14:20:00','2024-08-10 20:45:30'),('Flea and tick treatment','2hrs',1200,'1dddgg12-9iii-7ddd-ppp7-88aa4c5d6klm','a6d5c4b3-0g1f2e3d4-p3o2n1m0l9','2022-01-11 09:00:00','2023-09-22 06:00:00'),('Pet memorial services','3hrs',1200,'2sddff23-9iii-1zzz-bbn8-44cc1a2b9hgf','b1e4g2f3-5h6j7i8k0-9l2m1n3o4p','2022-01-02 08:30:15','2025-05-31 18:09:49'),('Pet nutrition counseling','5hrs',1300,'5wwwyy56-3ppp-1zzz-kkl9-66dd2e3f4nop','b7e6d5c4-1h2g3f4e5-q4p3o2n1m0','2022-01-10 15:30:45','2023-05-31 18:09:49'),('Pawdicure','5hrs',3600,'5ttggh56-6ppp-2ddd-kkl9-88vv5b3c6jkl','c2f1e5d3-6i7j8h9k0-1l4m2n3o5p','2022-01-13 12:34:56','2025-02-14 12:30:45'),('Blueberry facial','2hrs',1300,'9yyyff98-1uuu-6www-vpn5-55bb1c2d3qrs','c8f7e6d5-2i3h4g5f6-r5q4p3o2n1','2022-01-25 11:11:11','2025-05-31 18:09:49'),('Cat grooming','4hrs',1100,'1qqqaa12-8hhh-5rrr-ppp6-22dd4e5f9mno','d3g2f1e5-7j8k9i0h1-2l5m4n3o1p','2022-01-21 13:13:13','2023-10-31 23:59:59'),('Pet product sales','3hrs',1900,'4pppbb45-5hhh-3yyy-ccc2-33ee8a9b1tuv','d9g8f7e6-3j4i5h6g7-s6r5q4p3o2','2022-01-22 23:59:59','2024-05-31 18:09:49'),('Pet massage','4hrs',5000,'9wwwee98-3jjj-4yyy-lll5-77aa2b1c4pqr','e4h3g2f1-8k9j0i1h2-3m1n5o4p2','2022-01-08 11:11:11','2023-01-01 00:00:00'),('Pet massage','5hrs',1900,'4rrrff45-2uuu-7zzz-ccc2-99bb8c7d3stu','f5i4h3g2-9l0k1j2i3-4n2o1p5m3','2022-01-12 20:20:20','2024-01-01 00:00:00'),('cleaning trimming nails','3hrs',1200,'5b01bdef-da2c-4831-a6f4-305698e12a0b','f943a29a-c341-4527-9182-64cf9094a8d8','2023-06-01 10:05:06','2023-06-01 10:05:06'),('Pet training','2hrs',1100,'6tttyy67-1ppp-8www-fff3-11aa9b2c5vwx','g6j5i4h3-0m1l2k3j4-5o3p2n1m4','2022-01-14 18:00:00','2024-11-11 11:11:11'),('Pet cremation services','4hrs',5000,'3jjjdd34-5iii-6ddd-ooo4-33cc6a7b8zab','h7k6j5i4-1n2m3l4k5-6p4o3n2m1','2022-01-07 19:30:00','2023-11-11 11:11:11'),('Blueberry facial','2hrs',5000,'7uuukk78-9zzz-2yyy-rrr1-55ee0f1g2cde','i8l7k6j5-2o3n4m5l6-7q5p4o3n2','2022-01-22 23:59:59','2025-01-01 00:00:00'),('Ear cleaning','3hrs',1900,'2pppaa23-4hhh-5rrr-lll9-88dd5e6f7fgh','j9m8l7k6-3p4o5n6m7-8r6q5p4o3','2022-01-20 08:00:00','2023-05-31 18:09:49'),('Pet transportation','3hrs',1200,'1zzzbb12-6uuu-3ddd-ppp7-66cc3a4b5ijk','k0n9m8l7-4q5p6o7n8-9s7r6q5p4','2022-01-13 12:34:56','2025-03-05 08:15:30'),('Nail trimming and filing','5hrs',5000,'5dddff56-8iii-1www-kkl4-99bb2c3d6lmn','l1o0n9m8-5r6q7p8o9-a8s7r6q5p','2022-01-21 13:13:13','2024-10-31 23:59:59'),('Pet daycare','2hrs',1100,'9yyytt98-2ppp-7zzz-vpn5-77ee1b2c4opq','m2p1o0n9-6s7r8q9p0-b9a8s7r6q','2022-01-05 06:15:45','2024-04-20 16:20:00'),('Haircut and styling','3hrs',18000,'4hhhgg45-3uuu-4yyy-ccc2-22aa8b9c0rst','n3q2p1o0-7t8s9r0q1-c0b9a8s7r','2022-01-03 17:45:30','2024-10-31 23:59:59'),('Haircut and styling','4hrs',5000,'8wwwyy78-1iii-9ddd-fff6-44cc5a6b7uvw','o4r3q2p1-8u9t0s1r2-d1c0b9a8s7','2022-01-15 07:30:00','2024-04-20 16:20:00'),('Blueberry facial','5hrs',18000,'3rrraa34-7hhh-2rrr-ooo8-11dd0e1f2xyz','p5s4r3q2-9v0u1t2s3-e2d1c0b9a8s','2022-01-17 21:00:00','2023-02-14 12:30:45'),('Haircut and styling','3hrs',18000,'6zzzdd67-5ppp-8www-lll3-33bb9c1d4efg','q6t5s4r3-0w1v2u3t4-f3e2d1c0b9a','2022-01-15 07:30:00','2025-02-14 12:30:45'),('Pet chiropractic','2hrs',1300,'2dddff23-9iii-5zzz-bbn8-88cc1a2b3hij','r7u6t5s4-1x2w3v4u5-g4f3e2d1c0b','2022-01-27 16:00:00','2025-05-31 18:09:49'),('Pet product sales','3hrs',2500,'1wwwbb12-4uuu-6ddd-ppp7-77aa3c4d5klm','s8v7u6t5-2y3x4w5v6-h5g4f3e2d1','2022-01-26 22:22:22','2023-02-14 12:30:45'),('Pet daycare','4hrs',1200,'5yyytt56-2iii-1zzz-kkl9-99dd2e3f4nop','t9w8v7u6-3z4y5x6w7-i6h5g4f3e2','2022-01-01 12:00:00','2023-04-20 16:20:00'),('Pet boarding','2hrs',1300,'9pppff98-3uuu-7www-vpn5-22bb1c2d4qrs','u0x9w8v7-4a5z6y7x8-j7i6h5g4f3','2022-01-22 23:59:59','2023-12-25 08:00:00'),('Skunk odor removal','4hrs',18000,'4zzzgg45-1hhh-4yyy-ccc2-66ee8a9b0tuv','v1y0x9w8-5b6a7z8y9-k8j7i6h5g4','2022-01-19 19:19:19','2024-06-15 10:30:15'),('Feather extensions','4hrs',1300,'8dddyy78-6ppp-9www-fff6-33cc5b6c7wxy','w2z1y0x9-6c7b8a9z0-l9k8j7i6h5','2022-01-20 08:00:00','2024-04-20 16:20:00'),('Pet product sales','4hrs',5000,'3rrrdd34-2iii-2rrr-ooo8-44aa0e1f2zab','x3a2z1y0-7d8c9b0a1-m0l9k8j7i6','2022-01-14 18:00:00','2023-06-15 10:30:15'),('Anal gland expression','4hrs',1200,'6wwwtt67-8hhh-5ddd-lll3-11bb9c2d4efg','y4b3a2z1-8e9d0c1b2-n1m0l9k8j7','2022-01-06 14:20:00','2024-05-31 18:09:49'),('Pet cremation services','2hrs',1100,'2zzzff23-4uuu-8zzz-bbn8-77cc1a3b2hij','z5c4b3a2-9f0e1d2c3-o2n1m0l9k8','2022-01-30 12:00:00','2025-05-31 18:09:49');
/*!40000 ALTER TABLE `services` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `towns`
--

DROP TABLE IF EXISTS `towns`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `towns` (
  `name` varchar(40) NOT NULL,
  `county_id` varchar(100) NOT NULL,
  `id` varchar(40) NOT NULL,
  `created_at` datetime DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `county_id` (`county_id`),
  CONSTRAINT `towns_ibfk_1` FOREIGN KEY (`county_id`) REFERENCES `counties` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `towns`
--

LOCK TABLES `towns` WRITE;
/*!40000 ALTER TABLE `towns` DISABLE KEYS */;
INSERT INTO `towns` VALUES ('Shakahola','6faa9c56-28ee-4aaa-b67b-44ae1b9f5afc','2492bd46-be18-4f7d-8783-85fe46b22677','2023-06-01 09:21:05','2023-06-01 09:21:05'),('Nairobi','n1o2p3q4r5s6t7u8v9w0x1y2z3a4b5','aa9637d7-c806-4b1f-b15b-ce0772972426','2022-01-25 11:11:11','2023-01-01 00:00:00'),('Mombasa','aa9637d7-c806-4b1f-b15b-ce0772972426','bb9637d7-c806-4b1f-b15b-ce0772972426','2022-01-18 10:10:10','2023-07-04 14:00:00'),('Kisumu','d620617b-ce81-4fa1-be09-bb7ce950b465','cc9637d7-c806-4b1f-b15b-ce0772972426','2022-01-06 14:20:00','2023-03-05 08:15:30'),('Eldoret','b1c2d3e4f5g6h7i8j9k0l1m2n3o4p5','dd9637d7-c806-4b1f-b15b-ce0772972426','2022-01-16 16:45:00','2023-09-22 06:00:00'),('Nakuru','b1c2d3e4f5g6h7i8j9k0l1m2n3o4p5','ee9637d7-c806-4b1f-b15b-ce0772972426','2022-01-24 18:45:00','2025-05-31 18:09:49'),('Thika','n1o2p3q4r5s6t7u8v9w0x1y2z3a4b5','ff9637d7-c806-4b1f-b15b-ce0772972426','2022-01-06 14:20:00','2024-06-15 10:30:15'),('Malindi','aa9637d7-c806-4b1f-b15b-ce0772972426','gg9637d7-c806-4b1f-b15b-ce0772972426','2022-01-19 19:19:19','2024-12-25 08:00:00'),('Kitale','6faa9c56-28ee-4aaa-b67b-44ae1b9f5afc','hh9637d7-c806-4b1f-b15b-ce0772972426','2022-01-08 11:11:11','2023-11-11 11:11:11'),('Machakos','6faa9c56-28ee-4aaa-b67b-44ae1b9f5afc','ii9637d7-c806-4b1f-b15b-ce0772972426','2022-01-05 06:15:45','2025-02-14 12:30:45'),('Kericho','n1o2p3q4r5s6t7u8v9w0x1y2z3a4b5','jj9637d7-c806-4b1f-b15b-ce0772972426','2022-01-30 12:00:00','2025-05-31 18:09:49');
/*!40000 ALTER TABLE `towns` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-06-14  9:21:45
