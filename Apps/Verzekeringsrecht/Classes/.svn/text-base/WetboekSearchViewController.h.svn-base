//
//  WetboekSearchViewController.h
//  WetboekSearch
//
//  Created by rabshakeh on 6/15/09 - 1:09 PM.
//  Copyright __MyCompanyName__ 2011. All rights reserved.
//

#import <UIKit/UIKit.h>

@interface WetboekSearchViewController : UIViewController<UISearchBarDelegate, UITableViewDelegate, UITableViewDataSource> {
  IBOutlet UITableView    *myTableView ;
  IBOutlet UISearchBar    *searchBar ;
  NSMutableDictionary     *search_items ;
  UIActivityIndicatorView *progressIndicator ;
  NSString                *currentSearchText ;
  NSLock                  *myLock ;
}

@property (retain, nonatomic) NSLock                           *myLock ;
@property (retain, nonatomic) NSString                         *currentSearchText ;
@property (retain, nonatomic) UITableView                      *myTableView ;
@property (retain, nonatomic) UISearchBar                      *searchBar ;
@property (nonatomic, retain) IBOutlet UIActivityIndicatorView *progressIndicator ;

-(void)reloadDataTableViewWetboek ;

@end

