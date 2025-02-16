class FanAnalyser:
    def find_overlapping_fans(self, url_and_fans: list[dict[str, str]]) -> list[dict[str, str]]:
        """
        Find overlapping fans between multiple URLs.
        
        Args:
            fans (list): List of fans for each URL
            
        Returns:
            list: List of overlapping fans
        """
        min_overlap = 2
        fan_data = {} # {username: {url: url, profile_link: profile_link}}

        # count the number of times each fan appears
        for url, fans in url_and_fans.items():
            for fan in fans:
                username = fan['username']

                if username not in fan_data:
                    fan_data[username] = {
                        'urls': set(),
                        'profile_link': fan['profile_link']
                    }
                fan_data[username]['urls'].add(url)

        # filter out fans that don't meet the minimum overlap
        overlapping_fans = []
        for username, data in fan_data.items():
            if len(data['urls']) >= min_overlap:
                overlapping_fans.append({
                    'username': username,
                    'profile_link': data['profile_link'],
                    'urls': data['urls'],
                    'overlap_count': len(data['urls']),
                    'found_in': list(data['urls'])
                })

        
        return sorted(
            overlapping_fans,
            key=lambda x: x['overlap_count'],
            reverse=True
        )

    def format_results(self, overlapping_fans: list[dict[str, str]]) -> str:
        """
        Format the overlapping fans results for display.
        
        Args:
            overlapping_fans (list): List of overlapping fans
            
        Returns:
            str: Formatted results
        """
        if not overlapping_fans:
            print("No overlapping fans found.")
            return
        
        print("\nOverlapping Fans Found:")
        print("=" * 50)

        for fan in overlapping_fans:
            print(f"\nFan: {fan['username']}")
            print(f"Profile: {fan['profile_link']}")
            print(f"Found in {fan['overlap_count']}:")

            for url in fan['found_in']:
                print(f" - {url}")
            
            print("-" * 40)










